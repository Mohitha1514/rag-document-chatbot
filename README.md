# 📚 RAG Document Chatbot  
A Retrieval-Augmented Generation (RAG) chatbot using **Hugging Face**, **FAISS**, and **Gradio** to answer questions from your own documents.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-orange?style=for-the-badge)
![FAISS](https://img.shields.io/badge/Vector%20Search-FAISS-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## 🚀 Live Demo  
🔗 **Temporary Gradio Link (Colab):**  
`https://aa84b415606fb50cac.gradio.live/`

🔗 **Hugging Face Spaces Demo:**  
*(Coming soon)*

---

## 🧠 Overview  
This chatbot answers questions grounded **directly from your documents** using a Retrieval-Augmented Generation (RAG) pipeline.

### It works in 3 steps:
1️⃣ **Retrieve** → Find relevant document chunks using FAISS  
2️⃣ **Augment** → Pass retrieved data into the model  
3️⃣ **Generate** → FLAN-T5 creates the final answer  

This reduces hallucination and ensures high accuracy.

---

## 🏗️ Architecture  

Documents → Chunking → Embeddings (MiniLM) → FAISS Vector Search → FLAN-T5 → Answer

yaml
Copy code

---

## 🛠️ Tech Stack

### **Core Libraries**
- Hugging Face Transformers  
- Sentence Transformers  
- FAISS (Vector Search DB)  
- Gradio  
- PyTorch  

### **Models Used**
- **Embedding Model:** all-MiniLM-L6-v2  
- **Generator Model:** FLAN-T5-small  

---

## 📂 Project Structure  

rag-document-chatbot/
│
├── app.py # Gradio chatbot UI
├── ingest_index.py # Builds FAISS vector index
├── requirements.txt # Dependencies
├── README.md # Documentation
├── meta.json # Chunk metadata (auto-generated)
├── vector.index # FAISS index (auto-generated)
│
├── docs/ # Input documents
│ └── sample.txt
│
├── .gradio/ # Auto-created by Gradio
└── pycache/ # Auto-created

yaml
Copy code

---

## ▶️ How to Run Locally

### **1️⃣ Install dependencies**
```bash
pip install -r requirements.txt
2️⃣ Add your documents
Place .txt or .md files inside:

Copy code
docs/
3️⃣ Build FAISS index
bash
Copy code
python ingest_index.py --docs docs
This generates:

vector.index

meta.json

4️⃣ Run the chatbot
bash
Copy code
python app.py
Open the Gradio link shown (example: http://localhost:7860)

🧪 Features
✔ Uses your own documents
✔ Fast vector search using FAISS
✔ Context-grounded answers
✔ Lightweight & easy to run
✔ Beginner-friendly RAG pipeline

🔮 Future Enhancements
PDF ingestion (pdfplumber)

Reranker for improved accuracy

Multi-document chat history

Mistral / Llama-3 upgrade

Hugging Face Spaces deployment

👤 Author
Mohitha Papudesi
🔗 GitHub: https://github.com/Mohitha1514
🔗 LinkedIn: (https://www.linkedin.com/in/mohitha-papudesi)
