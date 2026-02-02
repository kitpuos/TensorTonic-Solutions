import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y, dtype = np.float64)
    
    if y.size == 0:
        return 0.0
    
    _, counts = np.unique(y, return_counts = True)

    total = counts.sum()
    if total == 0:
        return 0.0
    
    probs = counts / total
    probs = probs[probs > 0]
    entropy = - np.sum(probs * np.log2(probs))
    return entropy