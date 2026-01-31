import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs) == 0:
      return np.zeros((0, 0), dtype=int)
    
    if max_len is None:
      max_len = max(len(seq) for seq in seqs)
    
    padded_seqs = []
    for seq in seqs:
      truncated = seq[:max_len]
      padded = truncated + [pad_value] * (max_len - len(truncated))
      padded_seqs.append(padded)
    
    return np.array(padded_seqs, dtype = int)