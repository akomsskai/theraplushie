import whisper

# code to create audio file here

def speakToPlushie:
 
    whisperModel = whisper.load_model("medium")
    llmInput = whisperModel.transcribe(inputAudioFile)
    
    # return inputAudioFile