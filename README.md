# 🧠 Domain-Specific Retrieval-Augmented Generation (RAG) System

This project implements a **Retrieval-Augmented Generation (RAG)** system tailored for internal knowledge base queries using **LLaMA 2 7B** and **FAISS**. It retrieves domain-specific documents and generates context-aware responses, making it ideal for enterprise-level Q&A, support bots, or research assistants.

## 🚀 Features
- 🔍 Semantic Document Retrieval with FAISS
- 🧠 Contextual Answer Generation using LLaMA 2 7B
- 📄 Custom Document Loader support
- 🛠️ Modular and Extensible RAG pipeline
- 🧪 Ideal for internal tools and private datasets

## 🧰 Tech Stack
| Component             | Description                                        |
|----------------------|----------------------------------------------------|
| 🤗 Hugging Face       | LLaMA 2 integration for response generation       |
| 🔗 LangChain          | Orchestrates document loading and LLM pipelines   |
| 🔍 FAISS              | Vector similarity search for fast retrieval       |
| 🧬 SentenceTransformers | Converts documents into dense embeddings       |
## 📁 Project Structure
```
rag_pipeline/
├── data/                      # Your custom documents
├── embeddings/                # FAISS index and vector store
├── models/                    # LLaMA 2 weights (optional download path)
├── pipeline/
│   ├── loader.py              # Loads and preprocesses documents
│   ├── embedder.py            # Embeds using SentenceTransformers
│   ├── retriever.py           # FAISS-based retrieval logic
│   └── generator.py           # Generates final answers using LLaMA
├── app.py                     # Main application entry
├── requirements.txt
└── README.md
```

## 🔧 Running the App
```bash
python app.py
```

## 📌 Notes
- Ensure sufficient GPU memory (16GB+) for LLaMA 2 7B.
- Use `all-MiniLM-L6-v2` as a lightweight embedder.
- Documents must be `.txt` files in the `data/` directory.

## 🧑‍💻 Author
**Saad Saddique**  
AI/ML Developer | NLP Enthusiast

## 📜 License
MIT License

