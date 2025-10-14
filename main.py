import tkinter as tk
import pyttsx3
import speech_recognition as sr
from PIL import Image, ImageTk
import datetime
import webbrowser
import wikipedia
import os
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to respond to voice commands
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return None
    return command

# Function to handle the assistant's tasks
def handle_command(command):
    response = ""
    if 'hello' in command:
        response = "Hello! How can I assist you today?"
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        response = f"The current time is {current_time}"
    elif 'open' in command and 'google' in command:
        webbrowser.open("http://www.google.com")
        response = "Opening Google"
    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com')
        response = "Opening YouTube"
    elif 'play' in command:
        song = command.replace('play', '').strip()
        pywhatkit.playonyt(song)
        response = f"Playing {song} on YouTube."
    elif 'open' in command and 'calculator' in command:
        os.system("calc.exe")
        response = "Opening Calculator"
    elif 'open' in command and 'notepad' in command:
        os.system("notepad.exe")
        response = "Opening Notepad"
    elif 'search' in command:
        search_term = command.replace("search", "").strip()
        if search_term:
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open(search_url)
            response = f"Searching for {search_term} on Google."
        else:
            response = "Please specify what you want to search for."
    else:
        response = "I'm sorry, I didn't understand that."

    speak(response)
    result_label.config(text=response)

# Function to handle button click in GUI
def on_button_click():
    command = take_command()
    if command:
        handle_command(command)

# Create the GUI window
root = tk.Tk()
root.title("Personal Assistant")

# Load image for the window
try:
    image = Image.open(r"C:\Users\Bhanu Prakesh\Downloads\robo.jpeg")
    image = image.resize((150, 150))
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(root, image=photo)
    label_image.image = photo
    label_image.pack(pady=10)
except Exception as e:
    print(f"Error loading image: {e}")

# Add a label to display responses
result_label = tk.Label(root, text="I am your assistant. How can I help you?", width=50, height=4)
result_label.pack(pady=20)

# Add a button to trigger voice command
button = tk.Button(root, text="Speak", command=on_button_click, width=20)
button.pack(pady=10)

# Set window size and start GUI loop
root.geometry("600x400")
root.mainloop()
