def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    #Define a set of vowels
    vowels = set('aeiouAEIOU')

    #Use a dictionary comprehension to count the frequency of vowels
    vowel_freq = {char: phrase.lower().count(char) for char in vowels if char in phrase.lower()}
    return vowel_freq