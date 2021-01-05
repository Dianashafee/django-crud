from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
# Create your views here.


class HomeView(ListView):
    template_name = 'home.html'
    model = Blog

class BlogDetailsView(DetailView):
    template_name = 'post_detail.html'
    model = Blog

class BlogCreateView(CreateView):
    template_name = 'create.html'
    model = Blog
    fields = ['title', 'body', 'author']   

class BlogUpdateView(UpdateView):
    template_name = 'update.html'
    model = Blog
    fields = ['title', 'body']     

class BlogDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Blog
    fields = ['title', 'body', 'author'] 
    success_url = reverse_lazy('home')    