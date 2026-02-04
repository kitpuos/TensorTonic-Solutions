import numpy as np
def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    X = np.asarray(X, dtype = np.float64)
    H, W = X.shape

    out_h = (H - pool_size) // stride + 1
    out_w = (W - pool_size) // stride + 1
    output = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            h_start = i * stride
            w_start = j * stride

            window = X[h_start : h_start + pool_size, w_start : w_start + pool_size]
            output[i,j] = np.max(window)
    return output.tolist()