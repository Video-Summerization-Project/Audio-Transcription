import whisper
from datetime import timedelta
import time
import os

def format_timestamp(seconds):
    return str(timedelta(seconds=round(seconds, 2)))

def transcribe_chunks(
    chunk_paths,
    model_name="medium",
    language="ar",
    out_txt="combined_transcript.txt",
    out_srt="combined_transcript.srt"
):
    model = whisper.load_model(model_name)
    print(f"[🧠] Loaded Whisper model: {model_name}")
    index = 1
    global_start = 0

    with open(out_txt, "w", encoding="utf-8") as txt_out, open(out_srt, "w", encoding="utf-8") as srt_out:
        for chunk_path in chunk_paths:
            print(f"[🔍] Transcribing: {chunk_path}")
            result = model.transcribe(
                chunk_path,
                language=language,
                fp16=False,
                temperature=0,
                condition_on_previous_text=False,
                task="transcribe"
            )

            for seg in result["segments"]:
                start = seg["start"] + global_start
                end = seg["end"] + global_start

                # Write to SRT file
                srt_out.write(f"{index}\n")
                srt_out.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
                srt_out.write(f"{seg['text'].strip()}\n\n")

                # Write to TXT file
                txt_out.write(seg["text"].strip() + " ")

                index += 1

            # Calculate duration of current chunk to offset timestamps
            duration = whisper.audio.load_audio(chunk_path).shape[0] / 16000
            global_start += duration

    print(f"[✅] Transcription complete → {out_txt} + {out_srt}")

# ---------- Example usage ----------
if __name__ == "__main__":
    start = time.time()

    chunk_paths = ["chunks/chunk_000.wav", "chunks/chunk_002.wav"]
    transcribe_chunks(chunk_paths)

    end = time.time()
    print(f"Total time taken: {round(end - start, 2)} seconds")
