import whisper

# Load the model
model = whisper.load_model("base")

# Transcribe the audio
# Enter your audio path here
result = model.transcribe("exmple.mp3")

# Save the transcription to a file
with open("transcription.txt", "w") as f:
    f.write(result["text"])
