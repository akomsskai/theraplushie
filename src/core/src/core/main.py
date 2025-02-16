# from audio import *
from core.generateResponse import *
from elevenlabs import play

# change above import statements to be relative folders to main
def plushieProtocol():
    userInput = "Hi"

    while userInput != ("bye").lower():
        print("entered while loop")
        getResponse(userInput)
        # play(plushieResponse)
        # speakToPlushie()
        userInput = input()

    print("Exited")



