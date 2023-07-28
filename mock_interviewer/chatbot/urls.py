from django.urls import path
from .views import UserRegistration, UserLogin, ChatGPTAPI, SaveChat, ViewChat

urlpatterns = [
    path('user/register/', UserRegistration.as_view(), name='user-register'),
    path('user/login/', UserLogin.as_view(), name='user-login'),
    path('chat/gpt/', ChatGPTAPI.as_view(), name='chat-gpt'),
    path('chat/save/', SaveChat.as_view(), name='chat-save'),
    path('chat/view/', ViewChat.as_view(), name='chat-view'),
]