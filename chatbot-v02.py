from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
end_commands = ['exit', 'end', 'close', 'finish']

while True:
    user_input = input("Say anything: ")
    print(f"user: {user_input}")
    if user_input.casefold() in end_commands:
        break
    print(f"bot: {chatbot.get_response(user_input)}")
