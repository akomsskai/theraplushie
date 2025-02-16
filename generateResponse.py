import ollama
from dotenv import load_dotenv
from elevenlabs.client import Elevenlabs

def getResponse():
    # output = ollama.generate(model = "test1", prompt = input) 
    # where prompt is the user input sourced from @ miguel and model is the engineered model

    load_dotenv()

    client = ElevenLabs()
    """
    audioFile = client.text_to_speech.convert(
        text = input
        voice_id = 
        model_id = eleven_multilingual_v2
        output_format = 
    ) 
    """

    return audioFile

    # do something with audio file