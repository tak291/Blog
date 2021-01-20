#Here we import the models post and view templates.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


#Here we create the template for the home view.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'