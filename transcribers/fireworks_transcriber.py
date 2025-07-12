import os
import requests
import json

def transcribe_with_fireworks(
    file_path: str,
    api_key: str,
    model: str = "whisper-v3-turbo",
    vad_model: str = "silero",
    temperature: float = 0.0,
    timestamp_granularities: list = ["word"],
    endpoint: str = "https://audio-turbo.us-virginia-1.direct.fireworks.ai/v1/audio/transcriptions"
) -> dict:
    
    """
    Transcribes audio using Fireworks.ai Whisper API with optional word-level timestamps.

    Args:
        file_path (str): Path to the audio file (.mp3, .wav, .flac).
        api_key (str): Your Fireworks.ai API key.
        model (str): Whisper model name.
        vad_model (str): VAD model to use.
        temperature (float): Sampling temperature.
        timestamp_granularities (list): ["word"], ["segment"], or both.
        endpoint (str): API endpoint.

    Returns:
        dict: Transcription JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "rb") as f:
        response = requests.post(
            endpoint,
            headers={"Authorization": f"Bearer {api_key}"},
            files={"file": f},
            data={
                "model": model,
                "temperature": str(temperature),
                "vad_model": vad_model,
                "timestamp_granularities": timestamp_granularities  # Word-level timestamp support
            }
        )

    if response.status_code == 200:
        print("[✔] Transcription succeeded.")
        return response.json()
    else:
        print(f"[✘] Error {response.status_code}: {response.text}")
        raise RuntimeError("Transcription failed.")

# Example usage
if __name__ == "__main__":
    audio_file = "audio.mp3"

    result = transcribe_with_fireworks(audio_file, api_key=FIREWORKS_API_KEY)

    with open("fireworks_transcript.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
