stt.speak('Hello, what can I do for you?')
query = stt.listen()
print('query:', query)
print('Generating response...')


messages.append({"role": "user", "content": query[1]})
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=messages)

print(response.choices[0].message.content)
stt.speak(response.choices[0].message.content)
