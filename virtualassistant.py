# import the library needed for the virtual assistant

import speech_recognition as assistance
import pyttsx3

# now, let us obtain voice input from the microphone
listener = assistance.Recognizer()

# the next line is to initiate the pttsx3 library
engine = pyttsx3.init()
