# Audio Transcription

## How to Use

### 1. Clone the repository
```bash
git clone https://github.com/Video-Summerization-Project/Audio-Transcription
cd Audio-Transcription
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg
- Download FFmpeg from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
- Extract the ZIP file.
- Copy all files from the `bin` folder of FFmpeg into this project directory (same level as `main.py`).

### 5. Create a `.env` file
In the root of the repo, create a `.env` file containing:
```
GROQ_API_KEY=your_groq_key
FIREWORKS_API_KEY=your_fireworks_key
```

### 6. Configure your input video/audio
Open `main.py` and modify the `__main__` section with your file path:
```python
if __name__ == "__main__":
    path = "your_video/audio_path.mp4"
    transcribe_audio_in_chunks(Path(path), chunk_length=600, overlap=10, provider='groq', model="whisper-large-v3")
```

### 7. Run the script
```bash
python main.py
```

---

## Notes
- Input can be either video (`.mp4`) or audio (`.mp3`, `.wav`, etc.).
- Transcription is chunked to avoid model limits and ensure accuracy.
- Outputs are saved in the `output/` directory.

---
