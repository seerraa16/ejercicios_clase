def first_recurring(s):
    """
    Find the first recurring characters or None if there isn't one.

    >>> f("ABC")
    >>> f("ABAC")
    'A'
    >>> f("ABBAC")
    'A'
    >>> f("DADBBBC")
    'B'
    """
    lenght = len(s)
    chars = {(s.count(c), lenght - s.index(c)): c for c in s}
    first_recurring = max(chars.keys())
    if first_recurring[0] == 1:
        return None
    return chars[first_recurring]

