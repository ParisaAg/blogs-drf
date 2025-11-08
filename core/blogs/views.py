from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.list import ListView
from .models import Blogs 

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello World!'
        return context

class PostListView(ListView):
    model = Blogs
    queryset = Blogs.objects.all()
    paginate_by = 2
    ordering = ['-created_at']
    context_object_name = 'post_list'
    template_name = 'blogs/post_list.html'





class PostDetailView(DetailView):
    model = Blogs
    template_name = 'blogs/detail_post.html'
    context_object_name = 'post'



class PostCreateView(CreateView):
    model = Blogs
    template_name = 'blogs/create_post.html'
    fields = ['title', 'content','author','status','category','published_at']
    success_url = '/blogs/posts/'