
import faiss, pickle, os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def load_index():
    if not os.path.exists("index/esg.faiss"):
        from ingest import ingest
        ingest()
    index = faiss.read_index("index/esg.faiss")
    docs = pickle.load(open("index/docs.pkl", "rb"))
    return index, docs

index, docs = load_index()

def retrieve(query, k=5):
    q = model.encode([query])
    _, I = index.search(q, k)
    return [docs[i] for i in I[0]]
