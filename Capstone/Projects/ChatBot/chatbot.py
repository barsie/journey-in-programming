import json
from gtts import gTTS
import os

def load_brain():
    try:
        with open('brain.json', 'r') as file:
            brain = json.load(file)
    except FileNotFoundError:
        brain = {}
    
    return brain

def save_brain(brain):
    with open('brain.json', 'w') as file:
        json.dump(brain, file)
    

def get_response(user_input, brain):
    response = brain.get(user_input.lower())
    return response

def learn_new_phrase(user_input, brain):
    print(f"I don't know how to respond to '{user_input}'.")
    response = input(f"Please teach me how to respond to '{user_input}': ")

    brain[user_input.lower()] = response
    save_brain(brain)
    return response


def speak(response):
    tts = gTTS(response)
    tts.save("response.mp3")
    os.system("start response.mp3")


def main():
    brain = load_brain()
    print(f"Welcome! I'm Masi, your ChatBot. Type Bye to exit.")

    while True:
        user_input = input("[You]: ").strip().lower()
        if user_input == "bye":
            print(f"[Masi ChatBot]: Goodbye! Have a nice day!")
            speak("Goodbye! Have a nice day!")
            break
        response = get_response(user_input, brain)

        if response:
            print(f"[Masi ChatBot]: {response}")
            speak(response)
        else:
            response = learn_new_phrase(user_input, brain)
            print(f"[Masi]: {response}")
            speak(response)
            
if __name__ == "__main__":
    main()