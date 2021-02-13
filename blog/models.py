from django.db import models
from django.urls import reverse
from phone_field import PhoneField

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
    Employee_phone_number = PhoneField(blank=True, help_text='Employee phone.')        
    customer_number = PhoneField(blank=True, help_text='Customer phone')    
    addres = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")


    #Status of the job.
    OPEN = 1
    PENDING_APPOINTMENT =  2 
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



       


