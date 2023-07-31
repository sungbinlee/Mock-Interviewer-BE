from django.urls import path
from .views import UserRegistration, UserLogin, ChatGPTAPI

urlpatterns = [
    path('user/register/', UserRegistration.as_view(), name='user-register'),
    path('user/login/', UserLogin.as_view(), name='user-login'),
    path('chat/gpt/', ChatGPTAPI.as_view(), name='chat-gpt'),
]