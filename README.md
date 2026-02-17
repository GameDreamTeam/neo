# 🤖 ai — Local-First CLI AI Assistant

A fast, streaming, developer-focused AI assistant for the terminal.

Designed to feel like `git` or `kubectl`.

---

## 🚀 Overview

`ai` integrates a local LLM directly into your developer workflow.

### Core Features

- ⚡ Streaming responses
- 🧠 Interactive chat with history
- 📂 File analysis
- 🔌 Pipe support (Unix-style workflows)
- ⚙️ YAML-based configuration
- 🛠 Local LLMs via Ollama
- 🧩 Prompt-builder architecture

---

## ✨ Quick Start

```bash
ai chat
ai ask "hello"
ai summarize -f README.md
cat logs.log | ai debug
```

## 🛠 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/GameDreamTeam/ai-assistant.git
cd ai-assistant
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
```

Activate:

**Linux/macOS**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3️⃣ Install Package
```bash
pip install -e .
```

## 🧠 Install Ollama (Required)

### Option A — Native Install
Download: [https://ollama.com](https://ollama.com)

Pull a model:
```bash
ollama pull qwen2:0.5b
```

### Option B — Docker
```bash
docker run -d -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull qwen2:0.5b
```

### Verify
```bash
curl http://localhost:11434/api/tags
ai ask "Hello world!"
```

## ⚙️ Configuration

Config file location: `~/.ai/config.yaml`

Example:
```yaml
model: tinyllama
temperature: 0.2
max_tokens: 512
```

## 🏗️ Available Commands

| Command      | Description                          |
|--------------|--------------------------------------|
| `ai ask`     | Ask one-shot questions               |
| `ai chat`    | Interactive chat session             |
| `ai summarize` | Summarize files/text               |
| `ai explain` | Explain technical content            |
| `ai debug`   | Analyze logs (pipe-friendly)         |
| `ai fix`     | Analyze & fix configs/code           |

## 📌 Usage Examples

### Ask Questions
```bash
ai ask "Explain Kubernetes"
```

### Summarize File
```bash
ai summarize -f src/summarize.txt
```

### Explain Technical Content
```bash
ai explain -f src/mock/explain.txt
```

### Debug Logs (PRD Workflow)
```bash
cat mock/logs.log | ai debug
```

Example:
```bash
kubectl logs api-pod | ai debug
```

Output includes:
- Root cause
- Failure explanation
- Suggested fix
- Prevention tips

### Fix Configurations
```bash
ai fix -f src/nginx.conf
```

Returns:
- Issues found
- Corrected version
- Explanation