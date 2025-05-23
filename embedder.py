import os
import faiss
import numpy as np

def embed_documents(documents, save_path="embeddings/index.faiss"):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [doc.page_content for doc in documents]
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))
    
    # Save index
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    faiss.write_index(index, save_path)
    
    return embeddings, index

def load_faiss_index(path="embeddings/index.faiss"):
    if os.path.exists(path):
        return faiss.read_index(path)
    else:
        raise FileNotFoundError(f"No index found at {path}")
