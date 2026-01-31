import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.asarray(x, dtype = np.float64)

    ## first create the vectorized function, then call it on the array
    erf_vec = np.vectorize(math.erf)
    gelu = 0.5 * x * (1 + erf_vec(x / math.sqrt(2)))
    return gelu