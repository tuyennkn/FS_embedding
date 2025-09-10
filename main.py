from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

# Load model đa ngôn ngữ (cache sẵn để không reload mỗi request)
model = SentenceTransformer("intfloat/multilingual-e5-large")

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class BatchTextRequest(BaseModel):
    texts: list[str]

@app.post("/embed")
def get_embedding(request: TextRequest):
    embedding = model.encode([request.text])[0].tolist()
    return {
        "text": request.text,
        "embedding": embedding,
        "dimension": len(embedding)
    }

@app.post("/batch_embed")
def get_embedding_batch(request: BatchTextRequest):
    embeddings = model.encode(request.texts)
    return [
        {
            "text": text,
            "embedding": emb.tolist(),
            "dimension": len(emb)
        }
        for text, emb in zip(request.texts, embeddings)
    ]
