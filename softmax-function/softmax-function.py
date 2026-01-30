import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x, dtype = np.float64)

    ## For 1D, axis = 0
    if x.ndim == 1:
        vals = x - np.max(x, axis = 0)
        exp_x = np.exp(vals)
        return exp_x / np.sum(exp_x, axis = 0)
    
    ## For 2D, axis = 1, keepdims = True
    if x.ndim == 2:
        vals = x - np.max(x, axis = 1, keepdims = True)
        exp_x = np.exp(vals)
        return exp_x / np.sum(exp_x, axis = 1, keepdims = True)