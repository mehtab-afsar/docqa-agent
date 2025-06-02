from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import os
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()



import requests
from fastapi import Query
from xml.etree import ElementTree

@app.get("/arxiv_search/")
def arxiv_search(q: str = Query(..., description="Search query for Arxiv"), max_results: int = 5):
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": q,
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    resp = requests.get(url, params=params)
    # Parse XML feed
    tree = ElementTree.fromstring(resp.content)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    results = []
    for entry in tree.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        summary = entry.find('atom:summary', ns).text.strip()
        link = entry.find('atom:id', ns).text.strip()
        results.append({
            "title": title,
            "summary": summary,
            "link": link
        })
    return {"results": results}


# CORS for React frontend during dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = SentenceTransformer('all-MiniLM-L6-v2')

PDF_STORE = {}
# CHUNKS = []
# EMBEDDINGS = None

def chunk_text(text, chunk_size=500):
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    return chunks
from fastapi import UploadFile, File

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(content)

    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    os.remove(file_path)

    chunks = chunk_text(text, chunk_size=500)
    embeddings = MODEL.encode(chunks)

    PDF_STORE[file.filename] = {
        "chunks": chunks,
        "embeddings": embeddings
    }
    return {"message": f"Uploaded {file.filename} with {len(chunks)} chunks."}

from fastapi import Form
from typing import Optional

@app.post("/ask/")
async def ask_question(
    question: str = Form(...),
    pdf_name: Optional[str] = Form(None)
):
    if not PDF_STORE:
        return {"answer": "No documents uploaded yet."}

    # Search across all PDFs or just one
    results = []
    if pdf_name and pdf_name in PDF_STORE:
        docs = {pdf_name: PDF_STORE[pdf_name]}
    else:
        docs = PDF_STORE

    q_emb = MODEL.encode([question])[0]
    for name, data in docs.items():
        sims = np.dot(data["embeddings"], q_emb) / (
            np.linalg.norm(data["embeddings"], axis=1) * np.linalg.norm(q_emb) + 1e-8)
        idx = int(np.argmax(sims))
        score = sims[idx]
        answer = data["chunks"][idx]
        results.append({"pdf": name, "answer": answer, "score": float(score)})

    # Return the best overall result
    best = max(results, key=lambda x: x["score"])
    return {"answer": best["answer"], "pdf": best["pdf"], "score": best["score"]}
