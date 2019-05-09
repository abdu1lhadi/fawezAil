from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewCustomers

# Create your views here.

def home(request):
    if request.method == 'POST':
        comment_form = NewCustomers(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            comment_form = NewCustomers()
    else:
        comment_form = NewCustomers()
    context = {
        'title': 'HOME',
        'posts': Post.objects.all(),
        'comment_form': comment_form,
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'ABOUT US'})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    

    #check before save data from comment form
    if request.method == 'POST':
        comment_form = NewCustomers(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewCustomers()
    else:
        comment_form = NewCustomers()
    
    context = {
        'title': post,
        'post': post,
        'comment_form': comment_form,
    }
    
    return render(request, 'blog/detail.html', context)
