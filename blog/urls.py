from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:slug>/', views.blog, name='blog'),
    path('blog/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('category/<int:category_id>/', views.posts_by_category, name='category'),
    path('search/', views.search, name='search'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('about/', views.about_us, name='about'),
]