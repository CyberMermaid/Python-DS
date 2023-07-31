def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
    """
    # Create dictionary
    ltr_and_frequency = dict()
    # Iterate over every letter in phrase
    for ltr in phrase:
        # If ltr exists in ltr_and_frequency, increment the value of ltr by 1
        # Else, default=0 in get() so, value = 1 in ltr_and_frequency[ltr].
        ltr_and_frequency[ltr] = ltr_and_frequency.get(ltr, 0) + 1
    return ltr_and_frequency
