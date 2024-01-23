def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # Initialize an empty dictionary to store letter frequences
    letter_count = {}

    #Iterate through each character in the phrase
    for char in phrase:
        #Update the dictionary with the count of each letter (case-sensitive)
        letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count