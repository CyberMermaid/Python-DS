def intersection(l1, l2):
    """Return intersection of two lists as a new list::

    >>> intersection([1, 2, 3], [2, 3, 4])
    [2, 3]

    >>> intersection([1, 2, 3], [1, 2, 3, 4])
    [1, 2, 3]

    >>> intersection([1, 2, 3], [3, 4])
    [3]

    >>> intersection([1, 2, 3], [4, 5, 6])
    []
    """
    # l3 or third list is the intersection of l1 and l2
    l3 = [num for num in l1 and l2 if num in l1 and l2]
    return l3
