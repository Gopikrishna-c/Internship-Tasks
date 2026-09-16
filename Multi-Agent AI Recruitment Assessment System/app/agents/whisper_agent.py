import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path: str):
    result = model.transcribe(
        audio_path,
        fp16=False,      # CPU fix
        language="en"    # Interview language
    )

    return {
        "transcript": result["text"].strip(),
        "language": result["language"]
    }