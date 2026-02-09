def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here

    output = []
    step = chunk_size - overlap
    
    for i in range(0, len(tokens), step):
        output.append(tokens[i : i + chunk_size])
        if i + chunk_size >= len(tokens):
            break
    return output