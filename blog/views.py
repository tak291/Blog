#Here we import the models post and view templates.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView


#Here we create the template for the home view.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'    