import streamlit as st
import os
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.set_page_config(layout="wide")

DOCS_FOLDER = "docs"
DB_FOLDER = "chroma_db"

os.makedirs(DOCS_FOLDER, exist_ok=True)


# Session flag to avoid rebuilding DB repeatedly
if "ingested" not in st.session_state:
    st.session_state.ingested = False

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 📁 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload TXT / PDF / DOCX",
        type=["txt", "pdf", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files and not st.session_state.ingested:
        st.success("Uploading files...")

        for file in uploaded_files:
            with open(os.path.join(DOCS_FOLDER, file.name), "wb") as f:
                f.write(file.read())

        st.success("Building knowledge base...")

        all_docs = []

        for file in os.listdir(DOCS_FOLDER):
            path = os.path.join(DOCS_FOLDER, file)

            if file.endswith(".txt"):
                all_docs.extend(TextLoader(path).load())

            elif file.endswith(".pdf"):
                all_docs.extend(PyPDFLoader(path).load())

            elif file.endswith(".docx"):
                all_docs.extend(UnstructuredWordDocumentLoader(path).load())

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(all_docs)

        embeddings = OllamaEmbeddings(model="llama3")

        Chroma.from_documents(
            chunks,
            embeddings,
            persist_directory=DB_FOLDER,
            collection_name="learnvault"
        )

        st.session_state.ingested = True
        st.success("LearnVault updated")

    st.divider()
    

# ---------------- CHAT UI ----------------
st.markdown("<h1 style='text-align:center'>📚 LearnVault</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Your personal AI tutor</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask something...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    embeddings = OllamaEmbeddings(model="llama3")

    db = Chroma(
        persist_directory=DB_FOLDER,
        embedding_function=embeddings,
        collection_name="learnvault"
    )

    docs = db.similarity_search(question, k=2)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Answer ONLY using this context:

{context}

Question: {question}
"""

    llm = OllamaLLM(model="llama3")
    answer = llm.invoke(prompt)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()
