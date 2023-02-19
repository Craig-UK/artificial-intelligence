import speech_recognition
import pyttsx3
import sys

recogniser = speech_recognition.Recognizer()

while True:
    print('Running')
    try:
        with speech_recognition.Microphone() as mic:
            recogniser.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recogniser.listen(mic)

            text = recogniser.recognize_google(audio)
            text = text.lower()

            if 'exit' in text:
                print('Exiting')
                sys.exit()

            print(f"Recognised: {text}")

    except speech_recognition.UnknownValueError:
        recogniser = speech_recognition.Recognizer()
        print('Audio unkown. Try again.')
        continue