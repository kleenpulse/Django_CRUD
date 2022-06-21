from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

# Create your views here.


class PostListView(ListView):
    model = 'Post'


class PostCreateView(CreateView):
    model = 'Post'
    fields = '__all__'
    success_url: reverse_lazy("blog:all")


class PostListView(DetailView):
    model = 'Post'


class PostUpdateView(UpdateView):
    model = 'Post'
    fields = '__all__'
    success_url: reverse_lazy("blog:all")


class PostDeleteView(UpdateView):
    model = 'Post'
    fields = '__all__'
    success_url: reverse_lazy("blog:all")