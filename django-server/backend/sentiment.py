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

        sen = ""

        if sentiment >= -1 and sentiment <= -0.75:
            sen = "Extremely negative"
        elif sentiment >= -0.74 and sentiment <= -0.50:
            sen = "Very negative"
        elif sentiment >= -0.49 and sentiment <= -0.25:
            sen = "Negative"
        elif sentiment >= -0.24 and sentiment <= -0.01:
            sen = "Slightly negative"
        elif sentiment == 0:
            sen = "Neutral"
        elif sentiment >= 0.01 and sentiment <= 0.24:
            sen = "Slightly positive"
        elif sentiment >= 0.25 and sentiment <= 0.49:
            sen = "Positive"
        elif sentiment >= 0.50 and sentiment <= 0.74:
            sen = "Very positive"
        elif sentiment >= 0.75 and sentiment <= 1:
            sen = "Extremely positive"
        else:
            sen = "Error"

        return sen