def reverse_string(phrase):
    """Reverse string,

    >>> reverse_string('awesome')
    'emosewa'

    >>> reverse_string('sauce')
    'ecuas'
    """
    if len(phrase) != 0:
        # Convert the string phrase into a list called word
        word = list(phrase)
        # Reverse all the items in the list.
        word.reverse()
        # Convert the now reversed list called word into a string and return it
        return "".join(word)
