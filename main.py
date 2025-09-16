import os
import subprocess
import pdfplumber
import config   # 👈 import your config file

def run_ollama(prompt, model=config.MODEL_NAME):
    """Send prompt to Ollama model and return response text"""
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            capture_output=True,
            check=True
        )
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        return f"⚠️ Error running Ollama: {e}"

def extract_pdf_chunks(pdf_path, pages_per_chunk=config.PAGES_PER_CHUNK):
    """Yield text chunks of N pages each from the PDF"""
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)
        for start in range(0, num_pages, pages_per_chunk):
            end = min(start + pages_per_chunk, num_pages)
            text = ""
            for i in range(start, end):
                text += pdf.pages[i].extract_text() or ""
                text += "\n"
            chunks.append((start+1, end, text.strip()))
    return chunks

def main():
    chunks = extract_pdf_chunks(config.PDF_PATH, config.PAGES_PER_CHUNK)
    total_chunks = len(chunks)
    all_results = []

    for idx, (start, end, text) in enumerate(chunks, 1):
        print(f"\n--- Processing chunk {idx}/{total_chunks} (pages {start}–{end}) ---")
        if not text.strip():
            response = "[]  # No text found in these pages."
        else:
            prompt = config.PROMPT_TEMPLATE.format(start=start, end=end, chunk=text)
            response = run_ollama(prompt)
            if not response:
                response = "[]  # Model returned no output."

        print(response[:500] + ("..." if len(response) > 500 else ""))  # preview
        all_results.append(f"\n\n===== Chemical Analysis (Pages {start}–{end}) =====\n{response}")

    with open(config.OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(all_results))

    print(f"\n✅ Finished! Extracted chemical analysis saved to {config.OUTPUT_FILE}")

if __name__ == "__main__":
    main()
