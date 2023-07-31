def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.

        >>> triple_and_filter([1, 2, 3, 4])
        [12]

        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]

        >>> triple_and_filter([1, 2])
        []
    """
    # filtered_lst was a filter object that's been converted into a list
    filtered_lst = list(filter(lambda num: num % 4 == 0, nums))
    # triple_filtered_lst was a map object that's been converted into a list
    triple_filtered_lst = list(map(lambda a: a * 3, filtered_lst))
    return triple_filtered_lst
