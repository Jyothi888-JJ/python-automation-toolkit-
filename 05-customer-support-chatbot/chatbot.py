import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"need help", ["Sure, how can I assist you?"]],
    [r"price of", ["The price of the item is $50."]],
    [r"courses", ["If you are looking for DevOps and Cloud DevOps courses, check out devopsshack.com."]],
    [r"quit", ["Goodbye! Have a great day."]]
]

def run_chatbot():
    print("Welcome to Customer Support. Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

run_chatbot()
