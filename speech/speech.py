import speech_recognition
import pyttsx3
import sys
import pyttsx3 as tts
from textblob import TextBlob

recogniser = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 160)

while True:
    print('Please say a sentence: ')
    try:
        with speech_recognition.Microphone() as mic:
            recogniser.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recogniser.listen(mic)

            text = recogniser.recognize_google(audio)
            text = text.lower()

            if 'exit' in text:
                print('Exiting')
                sys.exit()

            blob = TextBlob(text)
            sentiment = blob.sentiment.polarity

            mood = None
            if sentiment < -0.5:
                mood = 'Really Negative'
            elif sentiment < 0.0:
                mood = 'Negative'
            elif sentiment == 0.0:
                mood = 'Neutral'
            elif sentiment > 0.0 and sentiment < 0.5:
                mood = 'Positive'
            elif sentiment > 0.5:
                mood = 'Really Positive'


            print(f"You just said: {text}, Sentiment Analysis Score: {sentiment}, What you just said was {mood}")
            speaker.say(f"You just said: {text}, Sentiment Analysis Score: {sentiment}, What you just said was {mood}")
            speaker.runAndWait()

    except speech_recognition.UnknownValueError:
        recogniser = speech_recognition.Recognizer()
        print('Audio unkown. Try again.')
        speaker.say("Audio unkown. Try again.")
        speaker.runAndWait()
        continue