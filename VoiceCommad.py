import pyttsx3
import wikipedia
import speech_recognition as sr


voice = pyttsx3.init('sapi5')
voices = voice.getProperty('voices')
voice.setProperty('voice',voices[1].id)
# query = str(input("Enter your command: "))
# result = wikipedia.summary(query, sentences=5)
# print(result)
# voice.say(result)
# voice.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        q_lower = query.lower()
        if 'what is' in q_lower:
            is_index = q_lower.index('what is')+ len('what is')
            sub = query[is_index:].strip()
        elif 'tell me about' in q_lower:
            about_index = q_lower.index('tell me about')+ len('tell me about')
            sub = query[about_index:].strip()            
        return sub 

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# print(takeCommand())
search = takeCommand()
say =wikipedia.summary(search, sentences=3)
print(say)
voice.say(say)
voice.runAndWait()
