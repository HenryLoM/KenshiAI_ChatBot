import pyttsx3

# make the object of tts
engine = pyttsx3.init()

# set a criterion of the speed
engine.setProperty('rate', 190)  # speed of speaking
engine.setProperty('voice', 'com.apple.eloquence.en-US.Fred')  # give a male voice

# start to speak
def start_talk(*words):
    text = str(words)
    engine.say(text)
    engine.runAndWait()

# if voice eas turned on
def warning():
    text = "Voice was turned on"
    engine.say(text)
    engine.runAndWait()