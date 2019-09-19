from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewCustomers, NewJob
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        comment_form = NewCustomers(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            comment_form = NewCustomers()
            messages.success(request,
                f'Thank you {new_comment}, Your request has been sent')
            
    else:
        comment_form = NewCustomers()
    context = {
        'title': 'HOME',
        'posts': Post.objects.all()[0:5],
        'comment_form': comment_form,
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'ABOUT US'})

def customs(request):
    return render(request, 'blog/customs.html', {'title': 'Customs'})

def equtpment(request):
    return render(request, 'blog/equtpment.html', {'title': 'Equtpment'})

def heavy_haulage(request):
    return render(request, 'blog/heavy_haulage.html', {'title': 'Heavy_Haulage'})

def jack_skidd(request):
    return render(request, 'blog/jack_skidd.html', {'title': 'Jack_Skidd'})

def job(request):
    if request.method == 'POST':
        job_form = NewJob(data=request.POST)
        if job_form.is_valid():
            new_job = job_form.save(commit=False)
            new_job.save()
            job_form = NewJob()
            messages.success(request,
                f'Thank you , Your request has been sent')
    else:
        job_form = NewJob()
    
    context = {
        'title': 'JOB',
        'job_form': job_form,
    }
    return render(request, 'blog/job.html', context)

def list_news(request):
    context = {
        'title': 'List News',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/listnews.html', context)

def transport(request):
    return render(request, 'blog/transport.html', {'title': 'Transport'})

def warehouse(request):
    return render(request, 'blog/warehouse.html', {'title': 'warehouse'})

def clients(request):
    return render(request, 'blog/clients.html', {'title': 'clients'})

def callus(request):
    return render(request, 'blog/callus.html', {'title': 'callus'})

def newrequest(request):
    if request.method == 'POST':
        comment_form = NewCustomers(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            comment_form = NewCustomers()
            messages.success(request,
                f'Thank you {new_comment}, Your request has been sent')
    else:
        comment_form = NewCustomers()
    context = {
        'title': 'newrequest',
        'comment_form': comment_form,
    }
    return render(request, 'blog/newrequest.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    

    #check before save data from comment form
    if request.method == 'POST':
        comment_form = NewCustomers(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            comment_form = NewCustomers()
            messages.success(request,
                f'Thank you {new_comment}, Your request has been sent')
    else:
        comment_form = NewCustomers()
    
    context = {
        'title': post,
        'post': post,
        'comment_form': comment_form,
    }
    
    return render(request, 'blog/detail.html', context)
