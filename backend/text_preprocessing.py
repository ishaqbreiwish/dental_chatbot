# Read and chunk texts
def process_text_file(filename, chunk_size=5):
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    
    # Combine lines into chunks with more context
    chunks = []
    for i in range(0, len(lines), chunk_size):
        chunk = ' '.join(lines[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks

texts = process_text_file("output.txt")

