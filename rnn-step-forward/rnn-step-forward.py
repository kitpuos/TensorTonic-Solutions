import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here

    x_t = np.asarray(x_t, dtype = np.float64)
    h_prev = np.asarray(h_prev, dtype = np.float64)
    b = np.asarray(b, dtype = np.float64)

    pre_act = x_t @ Wx + h_prev @ Wh + b
    h_t = np.tanh(pre_act)
    return h_t