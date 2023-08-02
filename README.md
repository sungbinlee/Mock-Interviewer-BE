# Mock-Interviewer-BE
## 프로젝트 개요
Mock Interview 프로젝트는 사용자가 가상의 면접을 경험하고, 인공지능(AI) 어시스턴트와 상호작용하여 면접 역량을 향상시킬 수 있는 웹 애플리케이션입니다. 사용자는 웹 브라우저를 통해 면접 과정을 진행하며, AI 챗봇이 면접관으로서 질문을 하고, 사용자는 면접자로서 답변을 제공합니다. AI 챗봇은 실시간으로 응답을 생성하고, 음성 출력 기능을 제공하여 사용자에게 음성으로도 면접 피드백을 제공합니다.

## Block Diagram
![voice_assisted_chatbot_block_diagram](https://github.com/sungbinlee/mock-interviewer/assets/52542229/50c0dee2-cb8e-4c4c-b97c-a70bbe32b139)

## Sequence Diagram 
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

3. 일일 채팅 제한: 사용자는 하루에 일정 횟수의 채팅만 가능합니다. 제한 횟수를 초과하는 경우 채팅이 불가능하도록 처리하여 서버 부하를 방지합니다.

4. AI 음성 출력 생성: AI 챗봇의 응답 텍스트를 음성 파일로 변환하여 사용자에게 제공합니다. 음성 출력 기능을 통해 사용자가 면접 피드백을 음성으로도 들을 수 있습니다.
