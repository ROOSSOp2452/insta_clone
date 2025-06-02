from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
    path('', views.inbox_view, name='inbox'),
   
    path('conversation/<str:username>/', views.conversation, name='conversation'), 
    path('chat/<str:username>/', views.chat_view, name='chat_view'),
    path('start/', views.start_conversation, name='start_conversation')# coming soon
]
