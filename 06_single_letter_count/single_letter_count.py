def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

    >>> single_letter_count('Hello World', 'h')
    1

    >>> single_letter_count('Hello World', 'z')
    0

    >>> single_letter_count("Hello World", 'l')
    3
    """
    # Create a new word that is lowercased for case-insensitivity
    new_word = word.lower()
    # Membership test
    if letter in new_word:
        return new_word.count(letter)
    else:
        return 0
