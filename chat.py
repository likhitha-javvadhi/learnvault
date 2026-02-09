from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma

llm = OllamaLLM(model="llama3")
embeddings = OllamaEmbeddings(model="llama3")

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

print("LearnVault ready. Ask questions (exit to quit).")

while True:
    q = input("\nYou: ")

    if q == "exit":
        break

    docs = db.similarity_search(q, k=2)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Answer using ONLY this context:

{context}

Question: {q}
"""

    answer = llm.invoke(prompt)
    print("\nLearnVault:", answer)
