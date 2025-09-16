# PDF Chemical Analysis Extractor (Ollama + LLMs)

A Python tool that extracts chemical-analysis results from PDF reports using a local LLM (Ollama + Mistral/Gemma etc.).  
It processes PDFs in configurable page-chunks, sends each chunk to a local Ollama model, and saves the extracted structured text to an output file.

---

## 🔧 What this README covers
- How to **download & install Ollama** (official site + commands)  
- How to **pull the Mistral model** to your machine  
- How to **edit `config.py`** (paths, model, prompt)  
- How to **run** the extractor  
- Troubleshooting & tips

---

## 📥 Download Ollama (official source)
Get the official Ollama installers and docs from the Ollama website: `https://ollama.com`. :contentReference[oaicite:0]{index=0}

- **Linux/macOS quick install** (runs the official install script):
```bash
# recommended for macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh
```
Open a terminal and run:
```bash
# example: pull the default Mistral model
ollama pull mistral
```
after that downloaded run:
```bash
ollama list
```
if it seems like mistral then the model is downloaded
now clone the repo and make virtual enviroment and run in the terminal of the IDE :
```bash
pip install -r requirements.txt
```
when all libraries are downloaded then you can run the app now with this in the terminal of the IDE :
```bash
python main.py
```
