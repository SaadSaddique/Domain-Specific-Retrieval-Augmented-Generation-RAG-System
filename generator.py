from transformers import pipeline

class LLMGenerator:
    def __init__(self, model_name="meta-llama/Llama-2-7b-hf"):
        self.generator = pipeline("text-generation", model=model_name, torch_dtype="auto", device_map="auto")

    def generate(self, query, documents):
        context = "\n".join(doc.page_content for doc in documents)
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        output = self.generator(prompt, max_new_tokens=150, do_sample=True)
        return output[0]['generated_text'].split("Answer:")[-1].strip()
