# LearnVault 📚🤖  
**RAG-based Personal AI Tutor**

LearnVault is a Retrieval-Augmented Generation (RAG) application that allows users to upload documents and ask questions based on their content.  
It uses **Streamlit** for UI, **Ollama** for local LLM inference, and **ChromaDB** for vector storage.

---

## 🚀 Features
- Upload TXT / PDF / DOCX documents
- Build a document-based knowledge base
- Ask contextual questions from uploaded documents
- Local LLM inference using Ollama (no cloud dependency)
- Clean and simple Streamlit UI

---

## 🛠 Tech Stack
- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB

---

## 📂 Project Structure
learnvault/
│── app.py # Streamlit UI
│── chat.py # Chat & response logic
│── ingest.py # Document ingestion & vector storage
│── requirements.txt
│── README.md
│── .gitignore


---

## ▶️ How to Run Locally

1️⃣ Install Ollama
Download and install Ollama from:  
https://ollama.com

Pull a model (example):
```bash
ollama pull llama3

Run Ollama (if not already running):

ollama serve

2️⃣ Clone Repository
git clone https://github.com/likhitha-javvadhi/learnvault.git
cd learnvault

3️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run Streamlit App
streamlit run app.py


Open browser:

http://localhost:8501
```

---

## 🖼 Screenshots

Screenshots are available inside the `/screenshots` folder:

- Project_structure.png  
- streamlit_run.png  
- Documents_loading.png  
- App_ui.png  
- App_result.png  

---

## ✨ Future Improvements

- User authentication  
- Better UI styling  
- Cloud deployment  
- Chat history persistence  

---

## 👩‍💻 Author

**Likhitha Javvadhi**

GitHub: https://github.com/likhitha-javvadhi
