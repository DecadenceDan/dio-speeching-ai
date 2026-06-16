import os
import tempfile
import sounddevice as sd
import soundfile as sf
import numpy as np
import whisper
from groq import Groq
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SAMPLE_RATE = 16000
DURATION = 5
WHISPER_MODEL = "base"

conversation_history = []


def record_audio(duration: int = DURATION, sample_rate: int = SAMPLE_RATE) -> str:
    print(f"\n🎙️  Gravando por {duration} segundos... Fale agora!")
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
    )
    sd.wait()
    print("✅ Gravação concluída.")
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    sf.write(tmp.name, audio, sample_rate)
    return tmp.name


def transcribe_audio(audio_path: str, model_name: str = WHISPER_MODEL) -> str:
    print("🔄 Transcrevendo com Whisper...")
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    text = result["text"].strip()
    print(f"📝 Você disse: {text}")
    return text


def chat_with_groq(user_message: str) -> str:
    conversation_history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Você é um assistente prestativo e conversacional. Responda de forma clara e concisa em português."},
            *conversation_history,
        ],
    )
    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})
    print(f"🤖 Resposta: {assistant_message}")
    return assistant_message


def text_to_speech(text: str, lang: str = "pt") -> None:
    print("🔊 Sintetizando voz com gTTS...")
    tts = gTTS(text=text, lang=lang, slow=False)
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(tmp.name)
    
    # Converte mp3 para wav e toca com sounddevice
    import subprocess
    wav_path = tmp.name.replace(".mp3", ".wav")
    subprocess.run(["ffmpeg", "-y", "-i", tmp.name, wav_path], 
                   capture_output=True)
    data, samplerate = sf.read(wav_path)
    sd.play(data, samplerate)
    sd.wait()
    
    try:
        os.unlink(tmp.name)
        os.unlink(wav_path)
    except PermissionError:
        pass


def run():
    print("=" * 50)
    print("  🎤 Voice ChatGPT — Whisper + Groq + gTTS")
    print("=" * 50)
    print("Pressione Ctrl+C para encerrar.\n")

    while True:
        try:
            input("Pressione ENTER para iniciar a gravação...")
            audio_path = record_audio()
            user_text = transcribe_audio(audio_path)
            os.unlink(audio_path)
            if not user_text:
                print("⚠️  Nenhuma fala detectada. Tente novamente.")
                continue
            response_text = chat_with_groq(user_text)
            text_to_speech(response_text)
        except KeyboardInterrupt:
            print("\n\n👋 Encerrando. Até mais!")
            break


if __name__ == "__main__":
    run()