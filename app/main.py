from fastapi import FastAPI, File, UploadFile
import speech
import translate

app = FastAPI()

@app.post("/translate")
async def translate_audio(file: UploadFile = File(...)):
    audio_path = f"temp.wav"
    
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    japanese_text = speech.speech_to_text(audio_path)
    english_text = translate.translate_text(japanese_text)

    return {
        "japanese": japanese_text,
        "english": english_text
    }
