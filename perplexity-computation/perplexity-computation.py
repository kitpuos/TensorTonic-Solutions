def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    n = len(actual_tokens)
    log_p = 0

    for i in range(n):
        p = prob_distributions[i][actual_tokens[i]]
        log_p += math.log(p)
    cross_entropy = - (log_p / n)
    perplexity = math.exp(cross_entropy)
    return perplexity