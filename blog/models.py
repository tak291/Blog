from django.db import models
from django.urls import reverse

# Create your models here.

#Test model.
class Post(models.Model):
    #To receiver the title and author. Author has a primary key
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    ) 

    #Intake the body of the blog
    body = models.TextField()
    

    #How to return the title of the blog to the users.
    def __str__(self):
        return self.title


    #Need to verify what this does exactly.
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])