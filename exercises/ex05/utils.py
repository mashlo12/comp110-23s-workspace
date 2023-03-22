"""'list' Utility Functions."""
__author__ = "730525708"


def only_evens(ints: list[int]) -> list[int]:
    """Return a new list containing only the even elements of lst."""
    idx: int = 0
    evens = []
    while idx < len(ints):
        x = ints[idx]
        if x % 2 == 0:
            evens.append(x)
        idx += 1
    return evens
    

def concat(first: list[int], second: list[int]) -> list[int]:
    """Return a new list containing elements of the first list followed by all of the elements of the second list."""
    all = []
    for i in first:
        all.append(i)
    for i in second:
        all.append(i)
    return all


def sub(ints: list[int], start: int, end: int) -> list[int]:
    """Return a subset of the given list between the start index and end index."""
    if start < 0:
        start = 0
    if end > len(ints):
        end = len(ints)
    if len(ints) == 0 or start >= len(ints) or end <= 0:
        return []
    idx: int = 0
    result = []
    while idx < len(ints):
        if (idx >= start) and (idx < end):
            result.append(ints[idx])
        idx += 1
    return result
