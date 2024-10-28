# 미니 ChatGPT와 대화하기
# step1
# 대화 입력
# ai_server의 함수에 전달
# 응답 받기
# 응답 출력
# -------
# step2
# 대화 반복

from openai.ai_server import gpt_robot

chat_data = [{"bot":"GPT는 실수할수 있습니다."}]

msg = input("메시지를 입력하세요: ")
chat_data.append({"human":msg})
robot_msg = gpt_robot(msg)
chat_data.append({"bot":robot_msg})

print("----------채팅화면-----------")
for data in chat_data:
    print(data)
