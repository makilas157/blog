from django.contrib import admin
from .models import Category, Blog, Comment, AboutUs, SocialLink


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
    list_filter = ('status', 'category', 'is_featured')
    search_fields = ('title', 'short_description', 'blog_body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'comment', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('comment',)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'link', 'created_at')
    list_filter = ('platform',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)