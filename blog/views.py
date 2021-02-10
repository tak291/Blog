#Here we import the models post and view templates.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Worker
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Here we create the template for the home view.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
   # template_name = 'login.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Worker
    template_name = 'post_new.html'
    fields = '__all__'    
    success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']     


class BlogDeleteView(DeleteView):
     model = Post
     template_name = 'post_delete.html'
     success_url = reverse_lazy('home')

