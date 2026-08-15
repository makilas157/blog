from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator  # <--- IMPORTANT: NEW IMPORT
from .models import Blog, Category, Comment, AboutUs, SocialLink


def home(request):
    """Homepage - shows featured and recent posts"""
    
    featured_posts = Blog.objects.filter(
        status='Published', 
        is_featured=True
    ).order_by('-created_at')
    
    posts = Blog.objects.filter(
        status='Published'
    ).exclude(
        is_featured=True
    ).order_by('-created_at')

    # ================= PAGINATION START =================
    paginator = Paginator(posts, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # ================= PAGINATION END =================
    
    context = {
        'featured_posts': featured_posts,
        'posts': page_obj,  # Changed from 'posts' to 'page_obj'
        'active_page': 'home',
    }
    return render(request, 'home.html', context)


def blog(request, slug):
    """Single blog post detail page"""
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    comments = Comment.objects.filter(blog=single_blog).order_by('-created_at')
    comment_count = comments.count()
    
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
        'active_page': 'blog',
        'active_category': single_blog.category.id,
    }
    return render(request, 'blog.html', context)


@login_required
def add_comment(request, slug):
    """Add comment to a blog post"""
    if request.method == 'POST':
        blog = get_object_or_404(Blog, slug=slug)
        comment_text = request.POST.get('comment', '').strip()
        
        if comment_text:
            Comment.objects.create(
                user=request.user,
                blog=blog,
                comment=comment_text
            )
            messages.success(request, '✅ Comment added successfully!')
        else:
            messages.error(request, 'Comment cannot be empty.')
    
    return redirect('blog', slug=slug)


def posts_by_category(request, category_id):
    """Filter posts by category"""
    category = get_object_or_404(Category, id=category_id)
    posts = Blog.objects.filter(
        category=category,
        status='Published'
    ).order_by('-created_at')

    # ================= PAGINATION START =================
    paginator = Paginator(posts, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # ================= PAGINATION END =================
    
    context = {
        'category': category,
        'posts': page_obj,  # Changed from 'posts' to 'page_obj'
        'active_category': category.id,
    }
    return render(request, 'posts_by_category.html', context)


def search(request):
    """Search posts by keyword"""
    keyword = request.GET.get('keyword', '').strip()
    
    if keyword:
        posts = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='Published'
        ).order_by('-created_at')
    else:
        posts = Blog.objects.filter(status='Published').order_by('-created_at')
    
    context = {
        'posts': posts,
        'keyword': keyword,
        'active_page': 'search',
    }
    return render(request, 'home.html', context)


def register(request):
    """User registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '✅ Registration successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {
        'form': form,
        'active_page': 'register',
    })


def about_us(request):
    """About Us page"""
    about = AboutUs.objects.first()
    return render(request, 'about.html', {
        'about': about,
        'active_page': 'about',
    })