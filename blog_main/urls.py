from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # <--- Add this line
    path('', include('blog.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
]