import whisper

# code to create audio file here
 

 
whisperModel = whisper.load_model("medium")
llmInput = whisperModel.transcribe(inputAudioFile)
return inputAudioFile