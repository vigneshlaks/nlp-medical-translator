import whisper

def transcribe_file(audio_file, model_name="base"):
    print("Loading Whisper model")
    model = whisper.load_model(model_name)
    
    print("Transcribing file")
    result = model.transcribe(audio_file)
    
    return result["text"]


if __name__ == "__main__":

    audio_path = "audio.mp3"
    
    transcription = transcribe_file(audio_path)
    
    print("\nTranscription:")
    print("-" * 50)
    print(transcription)
    print("-" * 50)