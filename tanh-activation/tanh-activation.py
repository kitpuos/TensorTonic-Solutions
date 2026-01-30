import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x, dtype = np.float64)
    if x.ndim == 0:
        x = x.reshape(1)
    ex1 = np.exp(x)
    ex2 = np.exp(-x)
    return (ex1 - ex2) / (ex1 + ex2)