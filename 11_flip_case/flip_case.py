def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    #Use a list comprehension to flip the case of each character based on the condition
    flipped_phrase = ''.join([char.swapcase() if char.lower() == to_swap.lower() else char for char in phrase])
    return flipped_phrase