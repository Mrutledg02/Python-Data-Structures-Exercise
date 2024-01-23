def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    #Use the all() function with isinstance to check if all items are lists
    return all(isinstance(item, list) for item in lst)