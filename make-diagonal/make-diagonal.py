import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.asarray(v, dtype = np.float64)
    matrix = np.zeros((v.size, v.size))
    np.fill_diagonal(matrix, v)
    return matrix