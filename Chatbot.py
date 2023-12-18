import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hello %1, how can I help you today?']],
    ['(hi|hello|hey|hola)', ['Hi there!', 'Hello!', 'Hey!']],
    ['(.*) your name?', ['I am a chatbot. You can call me Ali.']],
    ['(.*) (good|great|fine)', ['That\'s awesome!', 'Glad to hear that.']],
    ['(.*) (bad|sad)', ['I\'m sorry to hear that. How can I assist you?']],
    ['(.*) (age|old)', ['I\'m a chatbot, so I don\'t age!']],
    ['(.*) (created|made)', ['I was created using Python and NLTK.', 'I\'m the product of programming magic!']],
    ['exit', ['Goodbye!', 'Bye! Take care.']]
]

def basic_chatbot():
    print("Welcome to Chatbot! Type 'exit' to end the conversation.")
    print("Hello, I'm Bot How can I help you")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

basic_chatbot()
