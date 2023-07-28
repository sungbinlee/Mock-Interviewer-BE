# Mock-Interviewer-BE
모의 면접: ChatGPT를 이용한 챗봇 애플리케이션
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
