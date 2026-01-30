import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.asarray(x, dtype = np.float64)
    if x.ndim == 0:
        x = x.reshape(1)
    return np.maximum(0.0, x)