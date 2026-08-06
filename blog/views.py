from django.shortcuts import render, get_object_or_404
from .models import Blog, Category


def home(request):

    categories = Category.objects.all()

    featured_posts = Blog.objects.filter(
        is_featured=True,
        status="Published"
    )

    posts = Blog.objects.filter(
        is_featured=False,
        status="Published"
    )

    context = {
        "categories": categories,
        "featured_posts": featured_posts,
        "posts": posts,
    }

    return render(request, "home.html", context)


def posts_by_category(request, category_id):

    categories = Category.objects.all()

    category = get_object_or_404(Category, id=category_id)

    posts = Blog.objects.filter(
        category=category,
        status="Published"
    )

    context = {
        "categories": categories,
        "category": category,
        "posts": posts,
    }

    return render(request, "posts_by_category.html", context)