from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import views
# Create your views here.
from django.shortcuts import render

from .models import Post
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Like, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


@login_required
@login_required
def home_view(request):
    posts = Post.objects.all()

    for post in posts:
        post.liked_by_user = post.likes.filter(user=request.user).exists()  # Add this line
        post.all_comments = post.comments.all().order_by('created_at') 
        
    return render(request, 'home.html', {'posts': posts})
    
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # ✅ Use the correct field name
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'posts/home.html', {'posts': posts, 'comment_form': comment_form})

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('home')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    return redirect('home')
