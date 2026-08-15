from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # --- THIS IS THE NEW FIX ---
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    # ----------------------------

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50] + "..." if len(self.comment) > 50 else self.comment


# ========== NEW: About Us Model ==========
class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


# ========== NEW: Social Link Model ==========
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)  # GitHub, LinkedIn, YouTube, etc.
    link = models.URLField(max_length=200)
    icon = models.CharField(max_length=50, blank=True, null=True)  # Font Awesome icon name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return self.platform