from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from posts.models import Post, Like, Comment

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # home view to be created later
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(author=user).order_by('-created_at')

    for post in posts:
        post.total_likes = Like.objects.filter(post=post).count()
        post.comment_list = Comment.objects.filter(post=post).order_by('-created_at')

    return render(request, 'users/profile.html', {
        'profile_user': user,
        'posts': posts
    })

@login_required
def follow_toggle(request, username):
    target_user = get_object_or_404(User, username=username)
    
    if request.user == target_user:
        return redirect('profile', username=username)  # Prevent self-following
    
    if request.user in target_user.followers.all():
        target_user.followers.remove(request.user)
    else:
        target_user.followers.add(request.user)
    
    return redirect('profile', username=username)