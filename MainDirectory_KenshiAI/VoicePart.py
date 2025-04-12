import pyttsx3

# Make the object of tts and give it a certain voice
engine = pyttsx3.init()
engine.setProperty(name='voice', value='com.apple.speech.synthesis.voice.Fred')  # Give a male voice


def start_talk(*data):
    """Makes the text to be spoken."""
    text = str(data)
    engine.say(text[8:])
    engine.runAndWait()


def warning():
    """Says out loud if voice part was turned on."""
    text = "Voice was turned on"
    engine.say(text)
    engine.runAndWait()
