# 🎤 Voice ChatGPT

Conversa por voz com o ChatGPT usando **Whisper** (Speech-to-Text) e **gTTS** (Text-to-Speech).

## 🔄 Como funciona

```
Microfone → Whisper (STT) → ChatGPT API → gTTS (TTS) → Alto-falante
```

1. O usuário fala — o áudio é capturado pelo microfone
2. **Whisper** transcreve a fala para texto (suporta múltiplos idiomas)
3. O texto é enviado ao **ChatGPT** via API da OpenAI
4. A resposta é sintetizada em voz pelo **Google Text-to-Speech (gTTS)**

## 🛠️ Tecnologias

| Tecnologia | Papel |
|---|---|
| [Whisper](https://github.com/openai/whisper) | Speech-to-Text (ASR) |
| [ChatGPT (gpt-3.5-turbo)](https://platform.openai.com/docs) | Modelo de linguagem |
| [gTTS](https://gtts.readthedocs.io/) | Text-to-Speech |

## ⚙️ Pré-requisitos

- Python 3.9+
- Chave de API da OpenAI
- Microfone e alto-falante funcionando
- `ffmpeg` instalado (necessário para o Whisper)

### Instalando o ffmpeg

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Baixe em https://ffmpeg.org/download.html e adicione ao PATH
```

## 🚀 Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/voice-chatgpt.git
cd voice-chatgpt

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure a chave de API
cp .env.example .env
# Edite o .env e adicione sua OPENAI_API_KEY
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

## ⚙️ Configurações

No arquivo `src/main.py` você pode ajustar:

| Variável | Padrão | Descrição |
|---|---|---|
| `DURATION` | `5` | Segundos de gravação por turno |
| `WHISPER_MODEL` | `"base"` | Modelo Whisper (`tiny`, `base`, `small`, `medium`, `large`) |
| `lang` em `text_to_speech()` | `"pt"` | Idioma da síntese de voz |

> **Nota:** Modelos Whisper maiores são mais precisos, porém mais lentos. Para uso local, `base` ou `small` oferecem bom equilíbrio.

## 📁 Estrutura

```
voice-chatgpt/
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
