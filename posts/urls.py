from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, create_post  # ✅ Import create_post here
from . import views
urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_post, name='create_post'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),

]

# For serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
