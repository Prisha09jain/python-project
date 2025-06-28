import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking speed

# Speak Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen Function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results, check your internet.")
            return ""

# Respond to Commands
def respond(query):
    if "hello" in query:
        speak("Hello! How can I help you?")
    elif "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "date" in query:
        date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {date}")
    elif "search" in query:
        speak("What should I search for?")
        search_query = listen()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the search results for {search_query}")
    elif "exit" in query or "stop" in query:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't know how to help with that yet.")

# Main Loop
speak("Hi, I am your voice assistant!")
while True:
    query = listen()
    respond(query)
