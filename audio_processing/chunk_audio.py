import subprocess
import os

def get_audio_duration(input_audio):
    """
    Returns the duration of the audio file in seconds using ffprobe.
    """
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            input_audio
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return float(result.stdout.strip())

def chunk_audio(input_audio, number_of_chunks=5, output_dir="chunks"):
    """
    Split audio into equal-duration chunks based on total duration and desired number of chunks.
    """
    os.makedirs(output_dir, exist_ok=True)

    total_duration = get_audio_duration(input_audio)
    chunk_length = total_duration / number_of_chunks

    chunk_path_pattern = os.path.join(output_dir, "chunk_%03d.wav")

    cmd = [
        "ffmpeg", "-i", input_audio,
        "-f", "segment",
        "-segment_time", str(chunk_length),
        "-c", "copy",
        chunk_path_pattern
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    chunks = sorted([os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".wav")])
    print(f"[🎧] Audio of {round(total_duration, 2)} sec split into {len(chunks)} chunks → {output_dir}")
    return chunks


#chunk_audio("output_clean.wav", number_of_chunks=10, output_dir="chunks")