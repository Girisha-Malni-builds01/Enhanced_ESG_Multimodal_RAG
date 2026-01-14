
from transformers import pipeline
from retriever import retrieve

llm = pipeline("text-generation", model="google/flan-t5-base", max_new_tokens=256)

def answer(query):
    ctx = retrieve(query)
    prompt = f"Use only the context to answer.\nContext:\n{' '.join(ctx)}\nQ:{query}\nA:"
    return llm(prompt)[0]["generated_text"]
