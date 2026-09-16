import edge_tts
import os


async def text_to_speech(text: str, output_file: str):

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save(output_file)

    return output_file