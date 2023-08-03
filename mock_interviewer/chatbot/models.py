from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SOCIAL_PROVIDERS = (
        ('Kakao', 'Kakao'),
        # 추가적인 소셜 로그인 제공자를 필요에 따라 여기에 추가
    )
    
    social_provider = models.CharField(max_length=50, choices=SOCIAL_PROVIDERS, blank=True, null=True)
    social_uid = models.CharField(max_length=255, blank=True, null=True)
    daily_chat_limit = models.IntegerField(default=6)
    is_social_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('assistant', 'Assistant'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role} - {self.content}"


class UserChatRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
