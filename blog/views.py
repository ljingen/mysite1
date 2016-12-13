#coding:utf-8
from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post/list.html',{'posts':posts})

def post_detail(request, year, month, day, post):
    #post =get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year)
    print('----DEBUG: 我是post_detail，我被调用了 post的标题是:%s',post)
    return render(request, 'blog/post/detail.html', {'post': post})