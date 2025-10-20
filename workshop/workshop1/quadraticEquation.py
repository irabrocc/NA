def findRoots(a, b, c):

    import cmath

    # Calculate the discriminant
    D = b**2 - 4*a*c

    # Calculate the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(D)) / (2*a)
    root2 = (-b - cmath.sqrt(D)) / (2*a)

    return (root1, root2)