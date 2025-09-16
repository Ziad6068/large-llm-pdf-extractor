# config.py

# -----------------------------
# SETTINGS
# -----------------------------

# Path to your PDF
PDF_PATH = ""   

# Output file
OUTPUT_FILE = "report.txt"

# Model name (must be available in Ollama: e.g., "mistral", "gemma:2b", etc.)
MODEL_NAME = "mistral"

# Number of pages per chunk
PAGES_PER_CHUNK = 8

# -----------------------------
# Custom Prompt
# -----------------------------
PROMPT_TEMPLATE = """
Page range: {start}-{end}

Now extract from this chunk (pages {start}-{end}):

{chunk}
"""
