def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if not lst:
        # If the list is empty, return None
        return None
    else:
        # Return the last element of the list
        return lst[-1]