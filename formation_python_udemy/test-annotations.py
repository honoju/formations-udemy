def add(a :int = 0, b :int = 0) -> int :
    """addition de deux nombres

    Args:
        a (int, optional): le premier nombre. Defaults to 0.
        b (int, optional): le deuxieme nombre. Defaults to 0.

    Returns:
        int: la somme
    """
    print(a+b)
    return a+b

add(1, 2)