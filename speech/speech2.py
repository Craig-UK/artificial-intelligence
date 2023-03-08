import speech_recognition as sr
import pyttsx3 as tts
from textblob import TextBlob

r = sr.Recognizer()

#File must be in .wav format
#Put .wav file inside the speech folder and pass it in as string
#Example sr.AudioFile('test.wav')
audio_file = sr.AudioFile('')

with audio_file as source:
    audio = r.record(source)
    text = r.recognize_google(audio)

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    print(sentiment)