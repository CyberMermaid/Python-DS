from functools import reduce


def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1

    Original code without importing library before function:
    product = 1
    for num in nums:
        if num % 2 == 0:
            product *= num
    return product
    """

    """Initial value of product is 1. 
    If num from list nums is even then, multiply it with another even number a.
    """
    product = reduce(lambda num, a: num * a, filter(lambda num: num % 2 == 0, nums), 1)
    return product
