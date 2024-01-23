def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # Use string slicing to reverse the string
    reversed_phrase = phrase[::-1]
    return reversed_phrase