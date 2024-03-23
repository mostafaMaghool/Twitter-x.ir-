from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog/list.html'

def detail_view(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    context={
        "blog":blog,
    }
    return render(request,'blog/detail.html',context)