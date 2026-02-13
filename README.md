# 🤖 ai — Local-First CLI AI Assistant

A fast, streaming, developer-focused AI assistant built for the terminal.  
Designed to feel like `git` or `kubectl`.

---

## 🚀 Overview

`ai` integrates a local LLM directly into your developer workflows:

- ⚡ Streaming responses
- 🧠 Interactive chat with memory
- 📂 File analysis (`ai ask -f file.txt`)
- 🔌 Pipe support (`cat logs | ai ask`)
- ⚙️ YAML configuration
- 🛠 Local LLMs via Ollama

---

## ✨ Quick Start

```bash
ai chat                    # Interactive mode
ai ask -f README.md        # Analyze file
cat error.log | ai ask     # Pipe input
```

---

## 🛠 Installation

### 1️⃣ Clone & Setup

```bash
git clone https://github.com/GameDreamTeam/ai-assistant.git
cd ai-cli

# Create virtual environment
python -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows)
# .venv\Scripts\activate

# Install in editable mode
pip install -e .
```

---

### 2️⃣ Install Ollama (Required)

#### Option A: Native Install

1. Download from: https://ollama.com  
2. Pull a lightweight model:

```bash
ollama pull tinyllama
```

#### Option B: Docker

```bash
docker run -d -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull tinyllama
```

---

### 3️⃣ Verify Installation

```bash
curl http://localhost:11434/api/tags
ai ask "Hello world!"
```

---

## 🏗️ Commands

| Command            | Use Case                     |
|-------------------|------------------------------|
| `ai ask`          | One-shot questions           |
| `ai chat`         | Interactive sessions         |
| `ai ask -f file`  | File analysis                |
| `cat \| ai ask`   | Piped input                  |

---

## 🔧 Configuration

Create a config file at:

```
~/.ai/config.yaml
```

Example configuration:

```yaml
model: tinyllama
ollama_host: http://localhost:11434
```

---

## 📌 Example Usage

```bash
ai ask "Explain how Redis works"
ai ask -f error.log "Find the root cause"
git diff | ai ask "Summarize these changes"
```

---

## 🧠 Powered By

- Python
- Ollama
- Local LLMs

---

## 📄 License

MIT License