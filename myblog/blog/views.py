from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post, Subscription
from .forms import PostForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def subscribe(request, user_id):
    subscribed_user = User.objects.get(id=user_id)
    Subscription.objects.create(user=request.user, subscribed_to=subscribed_user)
    return redirect('home')

@login_required
def subscriptions_feed(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    posts = Post.objects.filter(author__in=[sub.subscribed_to for sub in subscriptions])
    return render(request, 'blog/subscriptions_feed.html', {'posts': posts})

def public_posts(request):
    posts = Post.objects.filter(is_public=True)
    return render(request, 'blog/public_posts.html', {'posts': posts})

@login_required
def request_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.is_hidden:
        return render(request, 'blog/request_post.html', {'post': post})
    return redirect('public_posts')

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

def home(request):
    posts = Post.objects.filter(is_public=True)
    return render(request, 'blog/home.html', {'posts': posts})
