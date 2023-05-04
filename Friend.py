import pyttsx3
friend = pyttsx3.init()
while True:
    speech = input("Say Something:")
    friend.say(speech)
    friend.runAndWait()
