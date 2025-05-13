import os
from pydub import AudioSegment
from datetime import timedelta
from pyannote.audio import Pipeline
from datetime import datetime
import whisperx

# ========== USER INPUT ==========
hf_token = os.getenv("HF_TOKEN")  # Make sure this is set or hardcode it
input_path = r"C:\Users\kazi7\Desktop\Meetingnotes5925.m4a" # file name goes here
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_dir = r"C:\Users\kazi7\Desktop\transcript"
output_txt_path = os.path.join(output_dir, f"transcript_{timestamp}.txt")
device = "cpu"  # or "cuda" if you have a compatible GPU
compute_type = "float32"  # required for CPU-only
model_size = "base"  # or "medium", "small", etc.
# ================================

# Step 1: Convert .m4a to .wav
def convert_to_wav(input_file):
    print("[INFO] Converting to WAV...")
    audio = AudioSegment.from_file(input_file)
    wav_path = os.path.splitext(input_file)[0] + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path

# Step 2: Transcribe audio
def transcribe_audio(wav_path):
    print("[INFO] Transcribing with WhisperX...")
    model = whisperx.load_model(model_size, device, compute_type=compute_type)
    result = model.transcribe(wav_path)
    return result["segments"], result["language"]

# Step 3: Diarize with PyAnnote
def diarize_audio(wav_path, hf_token):
    print("[INFO] Running speaker diarization...")
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=hf_token)
    diarization = pipeline(wav_path)
    return diarization

# Step 4: Assign speaker labels to transcript
def assign_speakers(segments, diarization):
    print("[INFO] Aligning transcription with speaker turns...")
    speaker_segments = []
    for segment in segments:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()

        # Find matching speaker from diarization
        matching_speaker = "Unknown"
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            if turn.start <= start <= turn.end:
                matching_speaker = speaker
                break

        start_time = str(timedelta(seconds=int(start)))
        end_time = str(timedelta(seconds=int(end)))
        speaker_segments.append(f"[{start_time} - {end_time}] {matching_speaker}: {text}")

    return "\n".join(speaker_segments)

# Step 5: Save transcript to file
def save_transcript(transcript, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript)
    print(f"[DONE] Transcript saved to {output_path}")

# === MAIN ===
if __name__ == "__main__":
    print("HF_TOKEN:", hf_token)
    wav_path = convert_to_wav(input_path)
    segments, lang = transcribe_audio(wav_path)
    diarization = diarize_audio(wav_path, hf_token)
    final_transcript = assign_speakers(segments, diarization)
    save_transcript(final_transcript, output_txt_path)
