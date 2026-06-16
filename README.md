# 🎤 dio-speeching-ai

Conversa por voz com IA usando **Whisper** (Speech-to-Text), **Groq + LLaMA 3** (LLM) e **gTTS** (Text-to-Speech).

## 🔄 Como funciona

1. O usuário fala — o áudio é capturado pelo microfone
2. **Whisper** transcreve a fala para texto (suporta múltiplos idiomas)
3. O texto é enviado ao **LLaMA 3** via **Groq API** (gratuito)
4. A resposta é sintetizada em voz pelo **Google Text-to-Speech (gTTS)**

## 🛠️ Tecnologias

| Tecnologia | Papel |
|---|---|
| [Whisper](https://github.com/openai/whisper) | Speech-to-Text (ASR) |
| [Groq + LLaMA 3](https://console.groq.com) | Modelo de linguagem (gratuito) |
| [gTTS](https://gtts.readthedocs.io/) | Text-to-Speech |

## ⚙️ Pré-requisitos

- Python 3.9+
- Chave de API da Groq (gratuita em console.groq.com)
- Microfone e alto-falante funcionando
- `ffmpeg` instalado

### Instalando o ffmpeg

```bash
# Windows
winget install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg
```

## 🚀 Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/DecadenceDan/dio-speeching-ai.git
cd dio-speeching-ai

# 2. Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure a chave de API
cp .env.example .env
# Edite o .env e adicione sua GROQ_API_KEY
```

## ▶️ Uso

### Modo voz (completo)

```bash
python src/main.py
```

Pressione **ENTER** para iniciar a gravação, fale por 5 segundos e aguarde a resposta.

### Modo texto (para testar sem microfone)

```bash
python examples/text_mode.py
```

## 📁 Estrutura

```
dio-speeching-ai/

├── src/

│   └── main.py          # Pipeline principal (voz completo)

├── examples/

│   └── text_mode.py     # Modo texto (sem microfone)

├── .env.example         # Exemplo de variáveis de ambiente

├── .gitignore

├── requirements.txt

└── README.md
```
## 📄 Licença

MIT