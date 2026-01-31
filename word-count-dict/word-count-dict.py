def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    
    frequency = dict()
    for sentence in sentences:
        for token in sentence:
            frequency[token] = frequency.get(token, 0) + 1
    return frequency