from django.contrib import admin
from .models import User, Chat, UserChatRequest

# Register your models here.
admin.site.register(User)
admin.site.register(Chat)
admin.site.register(UserChatRequest)