def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    output = []
    limit = math.sqrt(6 / fan_in)

    for i in range(len(W)):
        row = []
        for j in range(len(W[i])):
            w = W[i][j]
            scaled = w * 2 * limit - limit
            row.append(float(scaled))
        output.append(row)
    return output