import os

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def chunk_text(text, chunk_size=500):
    # Splits text into chunks of ~chunk_size characters, respecting line breaks
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

if __name__ == "__main__":
    input_path = os.path.join("..", "outputs", "sample.txt")
    output_path = os.path.join("..", "outputs", "sample_chunks.txt")

    text = read_text_file(input_path)
    chunks = chunk_text(text, chunk_size=500)

    # Save each chunk separated by a divider
    with open(output_path, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks):
            f.write(f"--- Chunk {i+1} ---\n")
            f.write(chunk + "\n\n")
    
    print(f"Text split into {len(chunks)} chunks and saved to {output_path}")
