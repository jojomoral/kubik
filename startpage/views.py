from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile, UserChats, Chat, Message


def test(request):
    context = {'Data': Test.objects.all()}
    return render(request, 'startpage/test.html', context)


def index(request):
    context = {'flash': '',}
    return render(request, 'startpage/index.html', context)

def user_page(request, user_id):
    user = Profile.objects.get(pk=user_id)
    context = {'Profile': user}
    return render(request, 'startpage/user.html', context)

def chat(request):
    current_user = request.user
    all_chats = []
    userchats = UserChats.objects.filter(user=current_user)
    for item in userchats:
        if item.chat.type == 'chat':
            other_user = Profile.objects.get(user=UserChats.objects.filter(chat=item.chat).exclude(user=current_user)[0].user)
            item.chat.title = f"{other_user.first_name} {other_user.last_name}"
        all_chats.append({'User': item.user,
                          'Chat': item.chat,
                          'Message': Message.objects.filter(chat=item.chat).latest('date'),
                          'Profile': other_user

                          })
    context = {'AllChats': all_chats,'User': current_user}
    return render(request, 'startpage/chat.html', context)

def send_message(request, chat_id):
    current_user = request.user
    text = request.POST.get('text')
    message = Message(chat=Chat.objects.get(pk=chat_id), from_user=current_user, text=text)
    message.save()
    return redirect(f'/chat/{chat_id}')


def current_chat(request, chat_id):
    current_user = request.user
    all_chats = []
    userchats = UserChats.objects.filter(user=current_user)
    for item in userchats:
        if item.chat.type == 'chat':
            other_user = Profile.objects.get(user=UserChats.objects.filter(chat=item.chat).exclude(user=current_user)[0].user)
            item.chat.title = f"{other_user.first_name} {other_user.last_name}"
        all_chats.append({'User': item.user,
                          'Chat': item.chat,
                          'Message': Message.objects.filter(chat=item.chat).latest('date'),
                          'Profile': other_user

                          })
    active_chat = Chat.objects.get(pk=chat_id)
    messages = Message.objects.filter(chat=active_chat)
    other_user = Profile.objects.get(user=UserChats.objects.filter(chat=active_chat).exclude(user=current_user)[0].user)
    context = {
                'ActiveChat':
                    {
                    'ChatTitle': f"{other_user.first_name} {other_user.last_name}",
                    'Chat': active_chat,
                    'Messages': messages,
                    'OtherUser': other_user
                    },
               'AllChats': all_chats,
                'User': current_user
                }
    return render(request, 'startpage/current_chat.html', context)


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    context = {}
    if user is not None:
        auth.login(request, user)
        return redirect(chat)
    else:
        context['flash'] = "Не верный логин или пароль"
        template = loader.get_template('startpage/index.html')

        return render(request, 'startpage/index.html', context)
