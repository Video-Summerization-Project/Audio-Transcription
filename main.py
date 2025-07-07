from audio_extractor import convert_audio_ffmpeg
from chunk_audio import chunk_audio
from transcriber import transcribe_chunks   


def run_transcription_pipeline(video_path):
    clean_audio = convert_audio_ffmpeg(video_path)
    #chunks = chunk_audio(clean_audio,number_of_chunks=5)
    transcribe_chunks(clean_audio )
if __name__ == "__main__":
    video_path = "video.mp4"  # Replace with your video file path
    run_transcription_pipeline(r'C:\Users\EL-Huda\Downloads\ITI\Final Project\chunks\chunk_001.wav')