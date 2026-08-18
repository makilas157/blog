from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Blog, Category, Comment, AboutUs, SocialLink
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

# ================= Dashboard View =================
@login_required
def dashboard(request):
    categories_count = Category.objects.all().count()
    posts_count = Blog.objects.all().count()

    context = {
        'categories_count': categories_count,
        'posts_count': posts_count,
    }

    return render(request, 'dashboard/dashboard.html', context)