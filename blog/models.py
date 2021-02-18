from django.db import models
from django.urls import reverse
from phone_field import PhoneField
import os
from twilio.rest import Client
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.

#Job model.
class Post(models.Model):
    #To receiver the title and worker
    # . Worker has a primary key
    job = models.CharField(max_length=200)
    worker = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    ) 

    customer_name = models.CharField(max_length=200, default=" ")
    Employee_phone_number = PhoneNumberField()        
    customer_number = PhoneNumberField()    
    addres = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    appointment_date = models.DateField(blank=True, null=True, default='mm/dd/yyyy')
    price = models.CharField(max_length=200, default="$")
    #tax = models.CharField(max_length=200, default='GSD')

    YES = 7
    NO =  8 


    PAYMENT_TYPE = (
        (YES, ' Yes'),
        (NO, 'No'),
        )

    GSD = models.IntegerField(choices=PAYMENT_TYPE, default=7)

    CASH = 4
    CARD =  5 
    TRANSFER = 6

    PAYMENT_TYPE = (
        (CASH, ' Cash'),
        (CARD, 'Card'),
        ( TRANSFER, 'Transfer' ),
        )

    payment = models.IntegerField(choices=PAYMENT_TYPE, default=4)

    OPEN = 1
    PENDING_APPOINTMENT = 2
    CLOSED = 3

    STATUS_CHOICE = (
        (OPEN, '    open'),
        (PENDING_APPOINTMENT, 'pending'),
        ( CLOSED, 'closed' ),
        )

    status = models.IntegerField(choices=STATUS_CHOICE,default=1)

    details = models.TextField()
 
    #How to return the title of the blog to the users.
    def __str__(self):
        return self.job


    #Return the id.
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


    def save(self, *args, **kwargs):

        if self.status == 1:

            # Your Account Sid and Auth Token from twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = 'AC62dc1020a3f092f7240a883688d2c13b'
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                                from_='+12183166789',
                                to='+19545731429',
                            )

            print(message.sid)
        
        return super().save(*args, **kwargs)

       


