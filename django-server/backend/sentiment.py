import speech_recognition as sr
import pyttsx3
import sys
import pyttsx3 as tts
from textblob import TextBlob
import os

def Sentiment(filename):
    r = sr.Recognizer()

    print(filename)

    script_dir = os.path.dirname(__file__)
    rel_path = "media/" + filename
    abs_file_path = os.path.join(script_dir, rel_path)

    print( abs_file_path)

    audio_file = sr.AudioFile(abs_file_path)

    with audio_file as source:
        audio = r.record(source)
        text = r.recognize_google(audio)

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        return sentiment