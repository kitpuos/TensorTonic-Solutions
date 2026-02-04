import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype = np.float64)
    y_pred = np.asarray(y_pred, dtype = np.float64)
    
    error = y_true - y_pred
    mod_error = np.abs(error)
    
    huber_loss = np.where(
        mod_error <= delta, 0.5 * (error) ** 2, delta * (mod_error - 0.5 * delta)
    )
    
    return np.mean(huber_loss)