from django.shortcuts import render
from .views import PostListView
from .models import Post
from. import views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home Directory'
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering  = ['-date_posted']


def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})
