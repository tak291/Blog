from django.db import models
from django.urls import reverse
from phone_field import PhoneField

# Create your models here.

#Job model.
class Post(models.Model):
    #To receiver the title and worker
    # . Author has a primary key
    job = models.CharField(max_length=200)
    worker = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    ) 

    #Intake the body of the blog
    details = models.TextField()
    customer_name = models.CharField(max_length=200, default="Cutomer name")
    Employee_phone_number = PhoneField(blank=True, help_text='Employee phone.')        
    customer_number = PhoneField(blank=True, help_text='Customer phone')    


    #How to return the title of the blog to the users.
    def __str__(self):
        return self.job


    #Need to verify what this does exactly.
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.job


    OPEN = 1
    PENDING_APPOINTMENT =  2 
    CLOSED = 3

    STATUS_CHOICE = (
        (OPEN, '    open'),
        (PENDING_APPOINTMENT, 'pending'),
        ( CLOSED, 'closed' ),
        )

    status = models.IntegerField(choices=STATUS_CHOICE,default=1)

    def __str__(self):
        if STATUS_CHOICE == 1:
            return ("Open")
        elif STATUS_CHOICE == 2:
            return ("Pending")
        else: 
            return("Closed")        
        