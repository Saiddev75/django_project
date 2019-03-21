from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
 

def blog_home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_home.html', context)



class PostListView(ListView):
    model =  Post
    template_name = 'blog/blog_home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' 
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model =  Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})


