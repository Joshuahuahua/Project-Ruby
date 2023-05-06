import stt
import openai
from time import sleep
from pynput.keyboard import Controller
keyboard = Controller()


api_key = None
with open('KEY', 'r') as f:
    api_key = f.readline()

openai.api_key = api_key

# {"role": "system",
#  "content": "You are a helpful assistant. Your answers should be short and concise, without sacrificing quality. After a question is answered, ask if there is anything else you can help with. When a conversation is finished, please end your message with 'end-conversation'."},
messages = [
    {"role": "system",
     "content": "If you are prompted to type something, encase the content in <text></text> tags (e.g. <text>Hello</text>. Make sure to give confirmation)."}
]


stt.speak('Hello there. What is your querey?')

while True:
    print(f"Listening...")
    query = stt.listen()
    print(f"Query: {query[1]}")

    messages.append({"role": "user", "content": query[1]})
    response_raw = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    response = response_raw.choices[0].message.content
    # print(response_raw)
    print(response)

    stt.speak(response)

    type_start = response.find('<text>')
    type_end = response.find('</text>')
    if type_start != -1 and type_end != -1:
        type_text = response[type_start+6:type_end]
        keyboard.type(type_text)

    if 'end-conversation' in response:
        break
    messages.append({"role": "assistant", "content": response})

print('Conversation ended.')
