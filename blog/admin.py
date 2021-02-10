from django.contrib import admin
from .models import Post, Worker
# Register your models here.


#Add model to DB.
admin.site.register(Worker)
admin.site.register(Post)