def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    dot_p = sum(a*b for a,b in zip(x1, x2))
    x1_norm = math.sqrt(sum(a*a for a in x1))
    x2_norm = math.sqrt(sum(b*b for b in x2))
    cosine_similarity = dot_p / (x1_norm * x2_norm)

    if label == 1:
        return 1 - cosine_similarity
    else:
        return max(0, cosine_similarity - margin)