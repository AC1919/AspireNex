# -*- coding: utf-8 -*-


def bot1(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "Doing great! How about you?"
    elif "your name" in user_input:
        return "My name is Simple!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure, what do you need assistance with?"
    else:
        return "Can you please say that again?"

while True:
    user_input = input("You: ")
    talk= bot1(user_input)
    print("Simple:", talk)
    if user_input.lower() in ["bye", "goodbye"]:
        break
