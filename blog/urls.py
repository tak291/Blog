from django.urls import path
from .views import (

    #Imported from my views that way they can be used.

    BlogListView, 
    BlogDetailView, 
    BlogCreateView, 
    BlogUpdateView, 
    BlogDeleteView,
)

#Patters for setting of urls.

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
   # path('post/login', BlogListView.as_view(), name='login'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]