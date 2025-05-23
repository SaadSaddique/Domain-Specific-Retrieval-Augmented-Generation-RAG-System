import os
from langchain_community.document_loaders import TextLoader

def load_documents(data_path):
    documents = []
    for filename in os.listdir(data_path):
        if filename.endswith(".txt"):
            path = os.path.join(data_path, filename)
            loader = TextLoader(path)
            documents.extend(loader.load())
    return documents