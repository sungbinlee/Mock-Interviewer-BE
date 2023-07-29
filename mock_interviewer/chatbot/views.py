from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Chat, UserChatRequest
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()


class UserRegistration(APIView):
    def post(self, request):
        # 요청으로부터 받은 데이터 추출
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        # 필수 필드가 있는지 확인
        if not username or not password or not email:
            return Response({'error': 'Username, password, and email are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # 이미 사용 중인 username인지 확인
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_409_CONFLICT)

        # 새로운 사용자 생성
        try:
            new_user = User.objects.create(
                username=username,
                password=make_password(password),
                email=email
            )
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 로그인 뷰
class UserLogin(APIView):
    def post(self, request):
        # 요청으로부터 받은 데이터 추출
        username = request.data.get('username')
        password = request.data.get('password')

        # 필수 필드가 있는지 확인
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # 사용자 인증
        user = authenticate(username=username, password=password)

        if user is not None:
            # 인증 성공 시 로그인 처리
            login(request, user)
            return Response({'message': 'User logged in successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

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