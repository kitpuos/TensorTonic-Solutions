def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    min_val = min(values)
    max_val = max(values)
    if min_val == max_val:
        return [0] * len(values)
    w = (max_val - min_val) / num_bins
    
    output = [num_bins - 1 if x == max_val else min((x - min_val) // w, num_bins - 1) for x in values]
    return output