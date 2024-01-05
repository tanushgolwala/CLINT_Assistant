import pyttsx3

def Speak(audio):
    voice = pyttsx3.init('sapi5')
    voices = voice.getProperty('voices')
    voice.setProperty('voice',voices[0].id)
    voice.say(audio)
    voice.runAndWait()
    