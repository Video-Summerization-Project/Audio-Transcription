from audio_processing.audio_extractor import convert_audio_ffmpeg
from audio_processing.chunk_audio import chunk_audio
from transcribers.groq_transcriber import transcribe_audio
from time import time


def run_transcription_pipeline(video_path, chunk = False, number_of_chunks = 5):
    clean_audio = convert_audio_ffmpeg(video_path)
    if chunk:
        chunks = chunk_audio(clean_audio,number_of_chunks= number_of_chunks)
        # chunk transcribe logic to be written

    transcribe_audio(clean_audio)

if __name__ == "__main__":
    start = time()
    video_path = "RawVideos\Linear Regression - Hesham Asem (720p, h264).mp4"  # Replace with your video file path
    run_transcription_pipeline(video_path)
    end = time()
    print(f"The Run Took {end-start: .2f} seconds")