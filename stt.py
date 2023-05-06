import win32com.client as wincl
import speech_recognition as sr


def listen(phrase=''):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize(audio)
        if phrase:
            if text.lower() != phrase.lower():
                return [False, text]
        return [True, text]
    except Exception as e:
        print(e)
        return None


def speak(phrase):
    speaker = wincl.Dispatch("SAPI.SpVoice")
    speaker.Speak(phrase)
