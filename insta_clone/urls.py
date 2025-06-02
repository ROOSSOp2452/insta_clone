# insta_clone/urls.py
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import home_view
from posts.views import home_view 
from django.conf import settings  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('messages/', include('messages_app.urls')), 
    path('', include('users.urls')),  # CHANGED from 'users/' to ''
    path('posts/', include('posts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
