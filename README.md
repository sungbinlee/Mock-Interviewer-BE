# Mock-Interviewer-BE
## 프로젝트 개요
Mock Interview 프로젝트는 사용자가 가상의 면접을 경험하고, 인공지능(AI) 어시스턴트와 상호작용하여 면접 역량을 향상시킬 수 있는 웹 애플리케이션입니다. 사용자는 웹 브라우저를 통해 면접 과정을 진행하며, AI 챗봇이 면접관으로서 질문을 하고, 사용자는 면접자로서 답변을 제공합니다. AI 챗봇은 실시간으로 응답을 생성하고, 음성 출력 기능을 제공하여 사용자에게 음성으로도 면접 피드백을 제공합니다.

## 기능 데모 

[프론트엔드 레포 바로가기](https://github.com/sungbinlee/Mock-Interviewer-FE)

https://github.com/sungbinlee/Mock-Interviewer-FE/assets/52542229/91c1f646-b7f0-48a8-8d47-a276f96e3f83

- AI 채팅: 사용자는 채팅 입력창을 통해 메시지를 작성하여 AI 어시스턴트와 대화할 수 있습니다. 작성한 메시지는 백엔드 API를 통해 AI에 전달되고, AI가 생성한 응답은 화면에 표시됩니다.

  - 채팅 히스토리: 사용자는 과거의 채팅 내용을 확인할 수 있습니다. 로그인 상태에서만 사용 가능하며, 채팅 기록이 없을 경우 "Start Interview" 버튼을 통해 새로운 인터뷰를 시작할 수 있습니다.

  - AI 음성 출력: AI가 생성한 응답은 텍스트 뿐만 아니라 음성으로도 재생될 수 있습니다. 사용자는 AI 응답의 텍스트를 읽지 않고도 음성으로 들을 수 있습니다.

  - 음성 입력 기능: 사용자는 음성 입력 버튼을 클릭하여 음성으로 메시지를 작성할 수 있습니다. 이를 통해 키보드를 사용하지 않고도 대화를 진행할 수 있습니다.

## 배포
- [배포 URL](https://chat.sungbinlee.dev)

- [프론트엔드](https://github.com/sungbinlee/Mock-Interviewer-FE)

- 배포환경
  - 백엔드 : AWS EC2, gunicorn, nginx
  - 프론트엔드 : Github Pages

## Block Diagram
아래는 블록 다이어그램으로 표현한 voice-assisted chatbot 앱의 동작과 구성을 설명합니다:

![voice_assisted_chatbot_block_diagram](https://github.com/sungbinlee/mock-interviewer/assets/52542229/50c0dee2-cb8e-4c4c-b97c-a70bbe32b139)

## Sequence Diagram 
아래의 시퀀스 다이어그램은 Frontend, Backend, OpenAI API, 그리고 TTS Engine 등의 컴포넌트들 간의 상호작용을 보여주고, 각 컴포넌트가 어떤 순서로 동작하는지를 명확하게 표현하여 시스템의 구조와 동작을 이해하는 데 도움을 줍니다.

![sequence_diagram](https://github.com/sungbinlee/mock-interviewer/assets/52542229/dd53bcb3-e95a-4982-9931-ebd93d7547b2)


1. Frontend(Github pages): 사용자 인터페이스를 제공하고, 사용자로부터 음성 입력 혹은 텍스트를 입력 받아 STT를 처리하고 Django 서버에 전송합니다.
2. Backend(Django): 프론트엔드로부터 요청을 받으면 OpenAI API로 전달합니다. OpenAI API로부터 받은 텍스트 응답을 TTS 엔진에 보내 음성으로 변환한 후 사용자에게 전달합니다.
3. OpenAI API: Django 서버가 전달한 텍스트 요청을 받아 ChatGPT 모델을 이용해 응답을 생성합니다.
4. TTS Engine: Django 서버로부터 받은 텍스트를 음성으로 변환하여 사용자에게 전달합니다.

> Frontend에서 음성 입력을 받아 STT를 이용하여 텍스트로 변환하고 Django 서버로 전송하면, Django 서버에서는 요청을 OpenAI API에 전달하여 응답을 받습니다. 그런 다음 Django 서버는 TTS 엔진을 사용하여 OpenAI API로부터 받은 텍스트 응답을 음성으로 변환하여 Frontend로 전달합니다.
## ER Diagram
![ChatERD](https://github.com/sungbinlee/Mock-Interviewer-BE/assets/52542229/b7a74158-65e6-4e62-b41f-717c3b6f8187)

기존 User 모델에 daily_chat_limit 필드가 추가되었습니다. 이 필드를 통해 유저별로 하루에 가능한 채팅 횟수를 설정할 수 있습니다.

## 백엔드 기능

1. 사용자 인증: 사용자 회원가입, 로그인, 로그아웃 기능을 제공합니다. 사용자의 입력 정보를 검증하고, 인증 성공 시 토큰을 발급하여 사용자 식별을 관리합니다.

2. AI 채팅 처리: 사용자가 입력한 메시지를 AI 어시스턴트에 전달하고, AI가 생성한 응답을 반환합니다. 사용자의 이전 채팅 기록을 불러와 채팅 히스토리를 확인할 수 있습니다.

3. 일일 채팅 제한: 사용자는 하루에 일정 횟수의 채팅만 가능합니다. 제한 횟수를 초과하는 경우 채팅이 불가능하도록 처리하여 서버 부하 및 과도한 과금을 방지합니다.

4. AI 음성 출력 생성: AI 챗봇의 응답 텍스트를 음성 파일로 변환하여 사용자에게 제공합니다. 음성 출력 기능을 통해 사용자가 면접 피드백을 음성으로도 들을 수 있습니다.
> 아래는 AI 챗봇의 텍스트 응답을 음성으로 변환한 실제 예시 음성 파일입니다.

https://github.com/sungbinlee/Mock-Interviewer-BE/assets/52542229/069485c0-8654-4fbf-b191-7f738726ef3e




## 토큰 인증 방식
토큰 인증 방식에는 Token Authentication 이 사용되었습니다. RESTful API에서 사용되는 인증 방식 중 하나로, 클라이언트가 토큰을 사용하여 인증을 처리하는 방법입니다. 이 방식은 브라우저 세션(Cookie)을 사용하지 않고, 클라이언트와 서버 간에 토큰을 주고받아 인증을 수행합니다. 아래는 Token Authentication의 기본적인 동작 방식에 대한 설명입니다.

### 기본 동작 방식
1. 클라이언트(사용자)가 로그인 또는 회원가입에 성공하면 서버에서 해당 유저에 대한 토큰을 생성합니다.
2. 서버는 생성된 토큰을 클라이언트에게 전달합니다.
3. 클라이언트는 이후 모든 요청에서 HTTP 헤더의 Authorization 필드에 생성된 토큰을 포함시켜 서버에 요청합니다.
4. 서버는 클라이언트로부터 받은 토큰을 검증하여 유효한 유저인지 확인합니다.
5. 토큰이 유효하고 인증이 성공하면 해당 요청을 처리합니다.
6. 토큰이 유효하지 않거나 인증이 실패하면 해당 요청을 거부합니다.

## API 정리
### 회원가입 (User Registration)
- URL: /api/user/register/
- Method: POST
- Description: 새로운 사용자를 등록하고 회원가입을 수행합니다.
- Request Body:
```json
{
  "username": "사용자이름",
  "email": "이메일주소",
  "password": "비밀번호"
}
```
- Response:
  - 성공적으로 회원가입한 경우
```json
{
  "message": "User registered successfully."
}
```
  - 이미 존재하는 사용자 이름 또는 이메일로 회원가입하려는 경우
```json
{
  "message": "Username already exists."
}
```
  - 필수 필드없이 회원가입 요청한 경우
```json
{
  "error": "Username, password, and email are required."
}
```
### 로그인 (User Login)
- URL: /api/user/login/
- Method: POST
- Description: 등록된 사용자가 로그인을 수행합니다.
- Request Body:
```json
{
  "username": "사용자이름",
  "password": "비밀번호"
}
```
- Response:
  - 로그인에 성공한 경우
```json
{
  "message": "User logged in successfully.",
  "Token": "사용자인증토큰"
}
```
  - 로그인에 실패한 경우
```json
{
  "error": "Invalid credentials."
}
```
### 로그아웃 (User Logout)
- URL: /api/user/logout/
- Method: GET
- Description: 로그인된 사용자를 로그아웃 처리하고 인증 토큰을 무효화합니다.
- Response:
```json
{
  "message": "User logged out successfully."
}
```
### 채팅 (Chat)
- URL: /api/chat/gpt/
- Method: GET, POST
- Description: 인공지능 채팅 AI와 사용자간의 채팅을 수행합니다.
- GET 요청
  - Description: 사용자의 채팅 기록을 가져옵니다.
  - Headers: Authorization: Token 사용자인증토큰
  - Response:
```json
{
  "conversations": [
    {
      "role": "user",
      "content": "사용자채팅메시지1"
    },
    {
      "role": "assistant",
      "content": "AI응답메시지1"
    },
    ...
  ],
  "count": "사용자 채팅 요청 횟수",
  "limit": "사용자 채팅 제한수"
}
```
- POST 요청
  - Description: 사용자가 AI에게 메시지를 보내고 응답을 받습니다.
  - Headers: Authorization: Token 사용자인증토큰
  - Request Body:
```json
{
  "user_input": "사용자입력메시지",
  "interview_topic": "인터뷰주제"
}
```
  - Response:
```json
{
  "response": "AI응답메시지",
  "audio_url": "AI응답음성URL"
}
```
  - 요청횟수가 제한횟수 이상 일 경우
```json
{
  "error": "You have exceeded the chat request limit for today."
}
```

## 설치 및 실행

1. 해당 프로젝트를 클론합니다.

```
git clone https://github.com/sungbinlee/Mock-Interviewer-BE.git
```

2. 가상환경을 생성하고 필요한 패키지를 설치합니다:

```
python -m venv venv
source venv/bin/activate  # Windows에서는 "venv\Scripts\activate" 실행
pip install -r requirements.txt
```

3. 데이터베이스를 마이그레이션합니다:

```
python manage.py migrate
```

4. 환경변수 파일을 작성합니다. (manage.py와 동일한 위치에)
```
vi .env
```
```
OPENAI_API_KEY="[사용자 API 키]"
DEBUG=True
SECRET_KEY="[사용자 시크릿 키]"
```

5. 개발 서버를 실행합니다:

```
python manage.py runserver
```

서버가 성공적으로 실행되면 브라우저에서 http://localhost:8000/ 으로 접속하여 API를 사용할 수 있습니다.
