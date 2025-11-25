# 📚 RAG Document Chatbot  
A Retrieval-Augmented Generation (RAG) chatbot using **Hugging Face**, **FAISS**, and **Gradio** to answer questions from your own documents.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-orange?style=for-the-badge)
![FAISS](https://img.shields.io/badge/Vector%20Search-FAISS-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## 🚀 Live Demo  
🔗 **Temporary Gradio Link (from Google Colab):**  
`https://YOUR-GRADIO-LINK-HERE.gradio.live`

🔗 **Hugging Face Spaces Demo (Coming Soon)**

---

## 🧠 Overview  
This project implements a **RAG pipeline**, allowing a user to ask questions based on the content of uploaded documents.

It works through:
- **Chunking text documents**
- **Creating embeddings using MiniLM**
- **Searching similar text using FAISS**
- **Answer generation using FLAN-T5**
- **A user-friendly Gradio interface**

This ensures responses are **grounded in your document context**, reducing hallucinations.

---

## 🏗️ Architecture  

Documents → Chunking → Embeddings → FAISS Index → Retriever → FLAN-T5 → Answer

---

## 🛠️ Tech Stack  
- Python  
- Hugging Face Transformers  
- Sentence Transformers  
- FAISS  
- Gradio  
- PyTorch  

**Models Used:**  
- Embeddings: `sentence-transformers/all-MiniLM-L6-v2`  
- Generator: `google/flan-t5-small`  

---

## 📂 Project Structure  

rag-document-chatbot/
│
├── app.py # Main Gradio chatbot UI
├── ingest_index.py # Builds FAISS index from docs
├── requirements.txt # Dependencies
├── README.md # Documentation
├── meta.json # Chunk metadata
├── vector.index # FAISS vector index (generated)
│
├── docs/ # Your documents go here
│ └── sample.txt
│
├── .gradio/ # Auto-created
└── pycache/ # Auto-created

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Add your documents

Place .txt or .md files inside the docs/ folder.

3️⃣ Build the vector index
python ingest_index.py --docs docs


This generates:

vector.index

meta.json

4️⃣ Run the chatbot
python app.py


Open the Gradio link (usually http://localhost:7860).
