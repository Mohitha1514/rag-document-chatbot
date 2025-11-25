
import json
import faiss
import gradio as gr
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GEN_MODEL = "google/flan-t5-small"  # use small in Colab for speed
INDEX_PATH = "vector.index"
META_PATH = "meta.json"
TOP_K = 3

embed_model = SentenceTransformer(EMBED_MODEL)
index = faiss.read_index(INDEX_PATH)
with open(META_PATH, "r", encoding="utf8") as f:
    meta = json.load(f)

tokenizer = AutoTokenizer.from_pretrained(GEN_MODEL)
gen_model = AutoModelForSeq2SeqLM.from_pretrained(GEN_MODEL)

def retrieve(query):
    q_emb = embed_model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(q_emb)
    _, I = index.search(q_emb, TOP_K)
    return [meta[int(idx)] for idx in I[0]]

def answer_question(query):
    hits = retrieve(query)
    context = "\\n\\n".join([h["text"] for h in hits])
    prompt = f"Context:\\n{context}\\n\\nAnswer the question using only this context. If not found, reply 'I don\\'t know'.\\n\\nQuestion: {query}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    outputs = gen_model.generate(**inputs, max_new_tokens=150)
    ans = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return ans

demo = gr.Interface(fn=answer_question, inputs=gr.Textbox(lines=2, placeholder="Ask your question..."),
                    outputs="text", title="RAG Document Chatbot")
if __name__ == "__main__":
    demo.launch()
