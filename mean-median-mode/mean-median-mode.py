import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)

    counts = Counter(x)
    mode = max(counts, key = counts.get)

    return (mean, median, mode)