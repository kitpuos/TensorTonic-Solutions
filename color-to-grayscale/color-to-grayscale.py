def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    
    output = []
    for i in range(len(image)):
        lst = []
        for j in range(len(image[i])):
            r, g, b = image[i][j]
            y = 0.299 * r + 0.587 * g + 0.114 * b
            lst.append(y)
        output.append(lst)
    return output