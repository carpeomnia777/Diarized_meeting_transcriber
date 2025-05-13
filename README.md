# 🎙️ Meeting Transcriber with Speaker Diarization (WhisperX + PyAnnote)

This tool turns your meeting recordings (e.g., .m4a) into speaker-labeled transcripts using WhisperX and PyAnnote.

---

## ✅ Features
- Converts .m4a to .wav
- Transcribes using WhisperX (OpenAI Whisper)
- Diarizes speakers using PyAnnote
- Outputs timestamped, speaker-labeled transcripts

---

## 🧰 Requirements
- Windows PC
- Internet access (first time setup)
- Hugging Face account (free)

---

## 🧪 Installation Steps

### 1. Install Python
Download: https://www.python.org/downloads/  
✅ Enable "Add to PATH" during install.

### 2. Install Git
Download: https://git-scm.com/download/win  
Accept all defaults.

### 3. Set Hugging Face Token
1. Create account: https://huggingface.co
2. Generate token: https://huggingface.co/settings/tokens
3. In Command Prompt:
```cmd
setx HF_TOKEN your_token_here
```

### 4. Install FFmpeg
1. Download ZIP: https://www.gyan.dev/ffmpeg/builds/
2. Extract to C:\ffmpeg
3. Add `C:\ffmpeg\bin` to your PATH
4. Restart Command Prompt
5. Check: `ffmpeg -version`

### 5. Install Python Dependencies
Open Command Prompt in the folder with the script and run:
```cmd
pip install -r requirements.txt
```

---

## 🚀 Usage

1. Place your `.m4a` file in the same folder.
2. Edit `test.py` and change the `input_path` to match your file name.
3. Run it:
```cmd
py test.py
```

Transcript will be saved with a timestamp in the same folder.

---

## 🧹 Troubleshooting

- `HF_TOKEN is None` → Recheck token setup and restart CMD.
- `ffmpeg not found` → Make sure `C:\ffmpeg\bin` is added to PATH.
- CPU is slow? Use a GPU and change `device = "cuda"` in the script.

---

## 🙏 Credits

- [WhisperX](https://github.com/m-bain/whisperx)
- [Whisper](https://github.com/openai/whisper)
- [PyAnnote](https://github.com/pyannote/pyannote-audio)
