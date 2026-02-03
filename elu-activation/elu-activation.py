import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    elu = [item if item > 0 else alpha * (math.exp(item) - 1) for item in x]
    return elu