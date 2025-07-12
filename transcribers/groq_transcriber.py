import time
import os
import json
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

def transcribe_audio(
    file_path: str,
    output_dir: str = "./transcripts",
    model: str = "whisper-large-v3-turbo"
) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    client = Groq()

    with open(file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=file,
            model=model,
            response_format="verbose_json",
            timestamp_granularities=["word"],
            temperature=0.0
        )

    json_path = os.path.join(output_dir, f"{base_name}.json")
    with open(json_path, "w", encoding="utf-8") as f_json:
            json.dump(transcription.model_dump(), f_json, indent=2, ensure_ascii=False, default=str)

    text_path = os.path.join(output_dir, f"{base_name}.txt")
    with open(text_path, "w", encoding="utf-8") as f_txt:
        f_txt.write(transcription.text)

    print(f"✅ Transcription saved:\n→ JSON: {json_path}\n→ Text: {text_path}")
    return transcription

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    audio_file = os.path.join(base_path, "output", "Linear Regression - Hesham Asem (720p, h264).wav")
    
    start = time.time()
    result = transcribe_audio(audio_file)
    end = time.time()
    print(f"The Run Took {end-start: .2f} seconds")
    #print(json.dumps(result, indent=2, default=str))
