import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.asarray(x, dtype = np.float64)
    q = np.asarray(q, dtype = np.float64)
    res = np.percentile(x, q, method = 'linear')
    return res