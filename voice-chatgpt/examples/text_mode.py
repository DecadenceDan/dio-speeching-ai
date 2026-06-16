"""
Modo texto — útil para testar sem microfone.
Você digita a pergunta e ouve a resposta em voz.
"""
import os
from gtts import gTTS
from openai import OpenAI
from playsound import playsound
import tempfile
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat(user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente prestativo."},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content


def speak(text: str, lang: str = "pt") -> None:
    tts = gTTS(text=text, lang=lang)
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(tmp.name)
    playsound(tmp.name)
    os.unlink(tmp.name)


if __name__ == "__main__":
    print("💬 Modo texto — digite sua pergunta (Ctrl+C para sair)\n")
    while True:
        try:
            question = input("Você: ").strip()
            if not question:
                continue
            answer = chat(question)
            print(f"🤖 ChatGPT: {answer}")
            speak(answer)
        except KeyboardInterrupt:
            print("\n👋 Até mais!")
            break
