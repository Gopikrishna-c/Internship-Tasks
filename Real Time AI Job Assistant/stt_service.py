from faster_whisper import WhisperModel


# Load Whisper model
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def speech_to_text(audio_file: str) -> str:

    segments, info = model.transcribe(
        audio_file
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()