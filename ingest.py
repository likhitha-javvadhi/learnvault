from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

print("Loading documents...")

DOCS_FOLDER = "docs"
all_docs = []

for file in os.listdir(DOCS_FOLDER):
    path = os.path.join(DOCS_FOLDER, file)

    if file.endswith(".txt"):
        loader = TextLoader(path)
        all_docs.extend(loader.load())

    elif file.endswith(".pdf"):
        loader = PyPDFLoader(path)
        all_docs.extend(loader.load())

    elif file.endswith(".docx"):
        loader = UnstructuredWordDocumentLoader(path)
        all_docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)

embeddings = OllamaEmbeddings(model="llama3")

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="./chroma_db"
)

print("LearnVault knowledge stored.")
