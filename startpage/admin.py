from django.contrib import admin

from .models import Chat, Profile, Message, UserChats

admin.site.register(Chat)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(UserChats)
