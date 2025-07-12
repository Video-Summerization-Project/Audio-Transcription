import subprocess
import os

def convert_audio_ffmpeg(input_file):
    file_name = input_file.split('\\')[-1].split('.')[0] + '.wav'
    output_file = os.path.join("output", file_name)
    cmd = [
        "ffmpeg", "-y", "-i", input_file,
        "-ac", "1",                        # mono channel
        "-ar", "16000",                   # 16kHz sample rate
        "-sample_fmt", "s16",            # 16-bit signed PCM
        "-vn",                            # disable video stream
        "-af", "highpass=f=200, lowpass=f=3000, dynaudnorm",  # audio filters
        "-map", "0:a",                    # map only the audio stream
        "-c:a", "flac",                   # encode audio as FLAC
        output_file
    ]

    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"[✔] Audio converted and cleaned → {output_file}")
    return output_file

if __name__ == "__main__":
    audio_path = convert_audio_ffmpeg("RawVideos\Optimization-Day05.mp4")
