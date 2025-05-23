from pipeline.loader import load_documents
from pipeline.embedder import embed_documents
from pipeline.retriever import Retriever
from pipeline.generator import LLMGenerator

# Load and embed documents
docs = load_documents("data/")
embeddings, faiss_index = embed_documents(docs)

# Initialize retriever and generator
retriever = Retriever(faiss_index, docs)
generator = LLMGenerator(model_name="meta-llama/Llama-2-7b-hf")

# Example query
query = "What is the protocol for sensor calibration?"
relevant_docs = retriever.retrieve(query)
response = generator.generate(query, relevant_docs)
print("\nAnswer:\n", response)