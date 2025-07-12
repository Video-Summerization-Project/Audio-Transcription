import os
from time import time

from dotenv import load_dotenv

from audio_processing.audio_extractor import convert_audio_ffmpeg
from audio_processing.chunk_audio import chunk_audio
from transcribers.groq_transcriber import transcribe_audio as transcribe_groq
from transcribers.fireworks_transcriber import transcribe_with_fireworks

# Load environment variables from .env
load_dotenv()
FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # optional

def run_transcription_pipeline(video_path, transcriber="groq", chunk=False, number_of_chunks=5):
    print(f"[•] Extracting and converting audio from {video_path}...")
    clean_audio = convert_audio_ffmpeg(video_path)

    if chunk:
        print(f"[•] Splitting audio into {number_of_chunks} chunks (not yet implemented)...")
        chunks = chunk_audio(clean_audio, number_of_chunks=number_of_chunks)
        print("[!] Chunk transcription is not supported yet.")
        return

    print(f"[•] Using transcriber: {transcriber}")

    if transcriber == "groq":
        result = transcribe_groq(clean_audio)
    elif transcriber == "fireworks":
        if not FIREWORKS_API_KEY:
            print("[!] FIREWORKS_API_KEY not found in .env")
            return
        result = transcribe_with_fireworks(clean_audio, api_key=FIREWORKS_API_KEY)
    else:
        print(f"[!] Unknown transcriber: {transcriber}")
        return

    print("[✔] Transcription complete.")
    return result

if __name__ == "__main__":
    start = time()

    video_path = r"RawVideos\Linear Regression - Hesham Asem (720p, h264).mp4"
    transcriber_choice = "fireworks"  # or "groq"
    chunk_audio_flag = False

    run_transcription_pipeline(
        video_path=video_path,
        transcriber=transcriber_choice,
        chunk=chunk_audio_flag,
        number_of_chunks=5
    )

    end = time()
    print(f"✅ Done in {end - start:.2f} seconds")
