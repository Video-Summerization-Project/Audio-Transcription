import subprocess
import os

def convert_audio_ffmpeg(input_file, output_file="output_clean.wav"):
    cmd = [
        "ffmpeg", "-y", "-i", input_file,
        "-ac", "1",
        "-ar", "16000",
        "-sample_fmt", "s16",
        "-vn",
        "-af", "highpass=f=200, lowpass=f=3000, dynaudnorm",
        output_file
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"[✔] Audio converted and cleaned → {output_file}")
    return output_file

audio_path = convert_audio_ffmpeg("video.mp4")
