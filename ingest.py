
from pathlib import Path
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss, pickle

PDF_DIR = Path("data/pdfs")
INDEX_DIR = Path("index")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def ingest():
    texts = []
    for pdf in PDF_DIR.glob("*.pdf"):
        reader = PdfReader(pdf)
        for p in reader.pages:
            t = p.extract_text()
            if t:
                texts.append(t)

    if not texts:
        return

    emb = model.encode(texts, show_progress_bar=False)
    index = faiss.IndexFlatL2(emb.shape[1])
    index.add(emb)

    INDEX_DIR.mkdir(exist_ok=True)
    faiss.write_index(index, str(INDEX_DIR / "esg.faiss"))
    pickle.dump(texts, open(INDEX_DIR / "docs.pkl", "wb"))

if __name__ == "__main__":
    ingest()
