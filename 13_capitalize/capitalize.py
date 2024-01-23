def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    #Use the 'capitalize' method to capitalize the first letter of the first word
    return phrase.capitalize()

    # or, doing it by hand:
    # return phrase[:1].upper() + phrase[1:]