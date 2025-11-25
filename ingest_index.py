
# ingest_index.py
import os, json
from glob import glob
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def chunk_text(text, chunk_size=200, overlap=40):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def load_plain_text_files(folder):
    docs = []
    for path in glob(folder + "/**/*.*", recursive=True):
        if path.lower().endswith((".txt", ".md")):
            with open(path, "r", encoding="utf8", errors="ignore") as f:
                docs.append({"path": path, "text": f.read()})
    return docs

def build_index(docs_folder="docs", index_out="vector.index", meta_out="meta.json"):
    docs = load_plain_text_files(docs_folder)
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    all_chunks = []
    meta = []
    for doc_id, doc in enumerate(docs):
        chunks = chunk_text(doc["text"])
        for chunk_id, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            meta.append({"doc_id": doc_id, "path": doc["path"], "chunk_id": chunk_id, "text": chunk})
    embs = model.encode(all_chunks, show_progress_bar=True, convert_to_numpy=True)
    faiss.normalize_L2(embs)
    d = embs.shape[1]
    index = faiss.IndexFlatIP(d)
    index.add(embs)
    faiss.write_index(index, index_out)
    with open(meta_out, "w", encoding="utf8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print("Index built:", index_out, meta_out)

if __name__ == "__main__":
    build_index("docs")
