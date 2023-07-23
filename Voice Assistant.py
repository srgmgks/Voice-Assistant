import speech_recognition as sr
import pyttsx3
import webbrowser

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User: {query}\n")
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Please try again.")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_query(query):
    if "hello" in query:
        speak("Hello! How can I assist you?")
    elif "goodbye" in query:
        speak("Goodbye! Have a nice day.")
        return True  
    elif "quit" in query or "exit" in query:
        speak("Okay, quitting the program.")
        return True  
    elif "open Google" in query:
        webbrowser.open("https://www.google.com")
    elif "open YouTube" in query:
        webbrowser.open("https://www.youtube.com/channel/UC8SxfmxHv7DSR3VSDHt5wrw")
    elif "open LinkedIn" in query:
        webbrowser.open("https://www.linkedin.com/in/srgmgks/")
    elif "open code" in query:
        webbrowser.open("https://github.com/srgmgks")
    elif "open hackerrank" in query:
        webbrowser.open("https://www.hackerrank.com/gokulakrishnanb7?hr_r=1")

def main():
    speak("Hello! I'm your voice assistant.")
    while True:
        query = listen()
        if query:
            should_exit = process_query(query)
            if should_exit:
                break

if __name__ == "__main__":
    main()
