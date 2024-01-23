def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if 1 <= day_of_week <= 7:
        # Using a list to map the day numbers to their names
        days_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        return days_of_week[day_of_week - 1]
    else:
        return None