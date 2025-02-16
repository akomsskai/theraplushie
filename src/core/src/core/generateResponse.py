import ollama
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

def getResponse(input):
    print("entered get response")
    output = ollama.chat(model = "theraplushie_7", 
                            messages = [{"role" : "user", "content" : input}])
    print(("ollama ran"))
    load_dotenv()

    client = ElevenLabs()
    print(output["message"]["content"])

    """audioFile = client.text_to_speech.convert(
        text = output
        voice_id = 5msz3SCgezg6jfzuHiRI
        model_id = eleven_multilingual_v2
        output_format = 
    ) 

    return audioFile"""
