# 📚 LearnVault

- Personal RAG-based AI tutor built with Python.
- It allows you to ask questions from your own notes using a local LLM.


## Features

- Ask questions from your own notes
- Retrieval Augmented Generation (RAG)
- Local LLM using Ollama (llama3)
- Vector database with Chroma
- Streamlit web UI

## Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB

## How to run

1. Install dependencies

pip install -r requirements.txt

2. Add your notes to docs/notes.txt

3. Ingest documents

python ingest.py

4. Run app

streamlit run app.py
