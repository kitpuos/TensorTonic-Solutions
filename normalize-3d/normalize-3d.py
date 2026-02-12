import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v, dtype = np.float64)
    norms = np.linalg.norm(v, axis = -1, keepdims = True)
    safe_norms = np.where(norms > 1e-10, norms, 1.0)
    normalised = v / safe_norms
    normalised = np.where(norms > 1e-10, normalised, 0.0)
    return normalised