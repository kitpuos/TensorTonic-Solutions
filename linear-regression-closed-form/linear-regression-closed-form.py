import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here

    X = np.asarray(X, dtype = np.float64)
    y = np.asarray(y, dtype = np.float64)

    X_T = np.transpose(X)
    inverse = np.linalg.inv(X_T @ X)
    
    w = inverse @ X_T @ y
    return w