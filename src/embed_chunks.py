import os
from sentence_transformers import SentenceTransformer
import pickle

def read_chunks(file_path):
    chunks = []
    with open(file_path, "r", encoding="utf-8") as f:
        current_chunk = ""
        for line in f:
            if line.startswith('--- Chunk'):
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                current_chunk = ""
            else:
                current_chunk += line
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
    return chunks

if __name__ == "__main__":
    input_path = os.path.join("..", "outputs", "sample_chunks.txt")
    output_path = os.path.join("..", "outputs", "chunk_embeddings.pkl")

    # Load text chunks
    chunks = read_chunks(input_path)

    # Load model (first time it will download, so may take 1-2 min)
    print("Loading sentence-transformers model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Generate embeddings
    print("Generating embeddings...")
    embeddings = model.encode(chunks)

    # Save embeddings and chunks together for later retrieval
    with open(output_path, "wb") as f:
        pickle.dump({'chunks': chunks, 'embeddings': embeddings}, f)

    print(f"Saved {len(chunks)} chunks and their embeddings to {output_path}")
