from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('chat/', views.chat,  name='chat'),
    path('chat/<int:chat_id>', views.current_chat, name='cur_chat'),
    path('chat/<int:chat_id>/send', views.send_message, name='send_message'),
    path('user/<int:user_id>', views.user_page, name='user_page')

]