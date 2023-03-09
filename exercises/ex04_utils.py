"""EX04 - 'list' Utility Functions."""

__author__ = "730525708"


def all(ints_list: list[int], num: int) -> bool:
    """Testing if every index in list and number are equal."""
    idx: int = 0
    if len(ints_list) == 0:
        return False

    while idx < len(ints_list):
        if num != ints_list[idx]:
            return False
        idx += 1
    return True


def max(max_list: list[int]) -> int:
    """Finding the largest in a list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    temp: int = max_list[0]
    idx: int = 0
    while idx < len(max_list):
        if temp < max_list[idx]:
            temp = max_list[idx]
        idx += 1
    return temp


def is_equal(first_list: list[int], sec_list: list[int]) -> bool:
    """Tests the equality of lists."""
    if len(first_list) != len(sec_list):
        return False
    idx: int = 0
    while idx < len(first_list):
        if first_list[idx] != sec_list[idx]:
            return False
        idx += 1
    return True