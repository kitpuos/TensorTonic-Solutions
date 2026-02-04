def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    ## f(x) = a * x**2 + b * x + c
    ## f'(x) = 2*a*x + b

    def f(x):
        return 2*a*x + b

    for i in range(steps):
        x0 -= lr * f(x0)
    
    return x0