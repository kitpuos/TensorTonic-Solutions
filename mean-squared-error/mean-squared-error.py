import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    n = len(y_true)
    sum_of_sq = 0
    for i in range(n):
        sum_of_sq += (y_pred[i] - y_true[i]) ** 2
    mse = sum_of_sq / n
    return mse