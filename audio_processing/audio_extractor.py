import subprocess
import os

def convert_audio_ffmpeg(input_file: str) -> str:
    """
    Converts the given audio or video file to a mono FLAC file at 16kHz,
    with filters applied for speech enhancement.

    Args:
        input_file (str): Path to the input audio or video file.

    Returns:
        str: Path to the converted FLAC file.
    """
    base_name = os.path.splitext(os.path.basename(input_file))[0] + '.flac'
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, base_name)

    cmd = [
        "ffmpeg", "-y", "-i", input_file,
        "-ac", "1",                        # mono channel
        "-ar", "16000",                   # 16kHz sample rate
        "-sample_fmt", "s16",             # 16-bit signed PCM
        "-vn",                             # remove video
        "-af", "highpass=f=200, lowpass=f=3000, dynaudnorm",  # speech cleanup
        "-map", "0:a",                     # select only audio stream
        "-c:a", "flac",                    # encode as FLAC
        output_file
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print("[✘] ffmpeg conversion failed:")
        print(result.stderr)
        raise RuntimeError("Audio conversion failed.")

    print(f"[✔] Audio converted and cleaned → {output_file}")
    return output_file


if __name__ == "__main__":
    audio_path = convert_audio_ffmpeg("RawVideos\Optimization-Day05.mp4")
