import nltk
from nltk.chat.util import Chat, reflections
print("Welcome to Basic Chatbot")
pairs = [["Hi. I want to chat", ["Hello. Let us chat"]],
['my name is (.*)', ['Hi %1']],
['(.*) your name', ['My name is Chaty']],
['How are you?', ['I am good']],
['(.*) do you do?', ['I am a simple chatbot']],
['(.*) created you?', ["Catherine created me using python and nltk"]],
['(.*) do you like?', ['I like chatting with people']],
['quit', ['see you soon. It was nice talking to you.']]]
chat = Chat(pairs, reflections)
chat.converse()