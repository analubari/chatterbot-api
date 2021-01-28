import json
import facebook
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

ACCESS_TOKEN = "EAAEi4hH3af8BAI45oZCDbZCmxFKykccUfcg5rzmjSffNcCBtRPTzV1ZCMBEpj0yVDSZBgALSoE9t6mLwHkcG118N5GKVD78sg8vLmTdtvrysommA3reFoXLTZCMg2dtnoGxSTukLcqxTCwn8EwiaD2shM70ELhzfzzXlr1cy96qY7cnyEXoRI"

def main():
    token = ACCESS_TOKEN
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='first_name, location, link, email, posts, friends')
    
    print('Printing profile: ')
    print(type(profile))
    print(json.dumps(profile, indent=4))
    print(type(json.dumps(profile, indent=4)))

if __name__ == '__main__':
    main()

""" 
chatbot = ChatBot('Crux')

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

peticion = input('Tú: ')
response = chatbot.get_response(peticion)
print(response)
"""