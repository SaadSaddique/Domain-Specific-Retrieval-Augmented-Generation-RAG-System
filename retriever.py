from sentence_transformers import SentenceTransformer
import numpy as np

class Retriever:
    def __init__(self, index, documents):
        self.index = index
        self.documents = documents
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def retrieve(self, query, top_k=3):
        query_vec = self.embedder.encode([query])
        D, I = self.index.search(np.array(query_vec), top_k)
        return [self.documents[i] for i in I[0]]