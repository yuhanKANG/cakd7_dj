from django.shortcuts import render
from blog.models import Post
# FBV (function based view). 파이썬파일(.py)
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )
    
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
