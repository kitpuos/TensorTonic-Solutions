def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    m = len(X)
    n = len(X[0])
    p = len(W[0])

    if n == len(W):
        Y = [[0 for _ in range(p)] for _ in range(m)]

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    Y[i][j] += X[i][k] * W[k][j]
                Y[i][j] += b[j]
        return Y