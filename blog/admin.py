from django.contrib import admin
from .models import Post
# Register your models here.


#Add model to DB.
admin.site.register(Post)