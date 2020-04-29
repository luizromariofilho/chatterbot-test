from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot = ChatBot("Ron Obvious")

trainer = ListTrainer(chatbot)

trainer.train(conversation)

while True:
    request = input("Input a question: ")
    response = chatbot.get_response(request)
    print(response)
