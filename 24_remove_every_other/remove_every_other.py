def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    #Use the list slicing to get every other item starting from index 0
    result = lst[::2]
    return result

    # Okay way
    #
    # return [val for i, val in enumerate(lst) if i % 2 == 0]