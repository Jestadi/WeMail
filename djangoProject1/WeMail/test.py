import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Capture speech from the command line microphone
with sr.Microphone() as source:
    print("Speak into the microphone:")
    audio = r.listen(source)

# Transcribe speech to text
try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error: {}".format(e))
