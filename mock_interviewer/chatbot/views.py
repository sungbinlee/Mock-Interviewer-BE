from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import User, Chat, UserChatRequest
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, get_user_model
import openai
import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

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
            token = Token.objects.create(user=new_user)
            return Response({'message': 'User registered successfully.', "Token": token.key}, status=status.HTTP_201_CREATED)
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
            token = Token.objects.get(user=user)
            return Response({'message': 'User logged in successfully.', "Token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        

class ChatGPTAPI(APIView):
    def get(self, request):
        print(request.user)
        user_chats = Chat.objects.filter(user=request.user).order_by('created_at')
        conversations = [{'role': chat.role, 'content': chat.content} for chat in user_chats]
        return Response({'conversations': conversations}, status=status.HTTP_200_OK)

    def post(self, request):
        # 요청으로부터 받은 데이터 추출
        user_input = request.data.get('user_input')
        chats = Chat.objects.filter(user=request.user).order_by('created_at')
        # 기존 채팅 내역과 새로운 채팅을 합침
        combined_chats = [{"role": chat.role, "content": chat.content} for chat in chats]

        # 시스템 시작 메시지 추가 (기존 채팅 내역이 없을 경우)
        if not user_input and not chats:
            system_start_message = {
                "role": "system", 
                "content": "I want you to act as an software engineer internship interviewer. I will be the candidate and you will ask me the interview questions for the position position. I want you to only reply as the interviewer. Do not write all the conservation at once. I want you to only do the interview with me. Ask me the questions and wait for my answers. Do not write explanations. Ask me the questions one by one like an interviewer does and wait for my answers. My first sentence is Hi'. Response with Korean"
            }
            combined_chats.append(system_start_message)
            # 시스템 저장
            ai_chat = Chat(user=request.user, role=system_start_message['role'], content=system_start_message['content'])
            ai_chat.save()

        # 사용자 입력을 채팅 내역에 저장
        if user_input:
            user_chat = {"role": "user", "content": user_input}
            combined_chats.append(user_chat)

            # 사용자 입력을 데이터베이스에 저장
            user_input_chat = Chat(user=request.user, role="user", content=user_input)
            user_input_chat.save()

        # 새로운 채팅 내역을 OpenAI API에 요청 보내기
        openai.api_key = env('OPENAI_API_KEY')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=combined_chats,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        ai_response = response['choices'][0]['message']['content']

        # AI 응답을 채팅 내역에 저장
        ai_chat = Chat(user=request.user, role="assistant", content=ai_response)
        ai_chat.save()

        # 응답값 프론트엔드로 전달
        return Response({'response': ai_response}, status=status.HTTP_200_OK)