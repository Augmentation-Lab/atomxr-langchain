from revChatGPT.V1 import Chatbot
import os
from dotenv import load_dotenv

load_dotenv()

email = os.environ.get('OPENAI_EMAIL')
password = os.environ.get('OPENAI_PASSWORD')

chatbot = Chatbot(config={
  "email": email,
  "password": password
})


def AskChat(prompt):
    prev_text = ""
    for data in chatbot.ask(prompt):
        message = data["message"][len(prev_text) :]
    return(message)

# print("Chatbot: ")
# prev_text = ""
# data = chatbot.ask("Hello, how are you?")
print(AskChat(input("human: ")))