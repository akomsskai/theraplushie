import ollama
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os

load_dotenv()
ELEVENLABS_API_KEY = os.environ.get("API_KEY")

def getResponse(input):
    output = ollama.chat(model = "theraplushie_7", 
                            messages = [{"role" : "user", "content" : input}])
    client = ElevenLabs(api_key = ELEVENLABS_API_KEY)    

    audioFile = client.text_to_speech.convert(
        text = output["message"]["content"],
        voice_id = "5msz3SCgezg6jfzuHiRI",
        model_id = "eleven_multilingual_v2",
        output_format = "mp3_44100_64",
    ) 

    play(audioFile)
    print(output["message"]["content"])
