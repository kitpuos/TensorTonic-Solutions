import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    
    vector = np.zeros(len(vocab), dtype = int)
    mapping = {word:i for i, word in enumerate(vocab)}

    for token in tokens:
        if token in mapping:
            vector[mapping[token]] += 1
    return vector