from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Chat, UserChatRequest

# 회원가입 뷰
class UserRegistration(APIView):
    def post(self, request):
        # 구현 로직
        pass

# 로그인 뷰
class UserLogin(APIView):
    def post(self, request):
        # 구현 로직
        pass

# ChatGPT로 요청 보내는 API 뷰
class ChatGPTAPI(APIView):
    def post(self, request):
        # 구현 로직
        pass

# 채팅 저장 뷰
class SaveChat(APIView):
    def post(self, request):
        # 구현 로직
        pass

# 채팅 조회 뷰
class ViewChat(APIView):
    def get(self, request):
        # 구현 로직
        pass