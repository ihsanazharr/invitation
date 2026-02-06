def modus(data):
    """
    Calculate the mode (modus) of a dataset.
    
    The mode is the value that appears most frequently in a dataset.
    
    Args:
        data: A list or iterable of values
        
    Returns:
        The mode value(s). If there are multiple modes, returns a list of all modes.
        Returns None if the dataset is empty.
        
    Examples:
        >>> modus([1, 2, 2, 3, 4])
        2
        >>> modus([1, 1, 2, 2, 3])
        [1, 2]
        >>> modus([5])
        5
        >>> modus([])
        None
    """
    if not data:
        return None
    
    # Count frequency of each value
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all values with maximum frequency
    modes = [value for value, freq in frequency.items() if freq == max_freq]
    
    # Return single value if only one mode, otherwise return list
    if len(modes) == 1:
        return modes[0]
    else:
        return sorted(modes)
