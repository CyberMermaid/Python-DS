def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

    >>> number_compare(1, 1)
    'Numbers are equal'

    >>> number_compare(-1, 1)
    'Second is greater'

    >>> number_compare(1, -2)
    'First is greater'
    """
    comparison = ""
    if a == b:
        comparison = "Numbers are equal"
    elif a > b:
        comparison = "First is greater"
    else:
        comparison = "Second is greater"
    return comparison
