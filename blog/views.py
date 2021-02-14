#Here we import the models post and view templates.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm

#Here we create the template for the home view.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


#To view the details of the job.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


#Job creation with the form view.
class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'
 
    success_url = reverse_lazy('home')

#This is the view to edit the post.
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = '__all__'     

#This is the view to delete the post.
class BlogDeleteView(DeleteView):
     model = Post
     template_name = 'post_delete.html'
     success_url = reverse_lazy('home')

