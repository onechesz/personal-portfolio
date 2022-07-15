from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    db_blogs = Blog.objects.order_by('-date')

    return render(request, 'blog/blogs.html', {'blogs': db_blogs})


def blog_info(request, blog_id: int):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/blog_info.html', {'blog': blog})
