"""EX04 - `list` Utility Functions."""
__author__ = "730525708"


def all(ints_list: list[int], num: int) -> bool:
    """Finding if all the ints in a list are the same as num."""
    idx: int = 0
    if len(ints_list) == 0:
        return False
    
    while idx < ints_list[idx]:
        if ints_list[idx] != num:
            return False
        idx += 1
    return True


def max(max_list: list[int]) -> int:
    """Finding the largest number in the list"""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    temp: int = max_list[idx]
    while idx < len(max_list):
        if temp < max_list[idx]:
            temp = max_list[idx]
        idx += 1
    return temp


def is_equal(first_list: list[int], sec_list: list[int]) -> bool:
    """Finding if every element at every index is equal in both lists"""
    if len(first_list) != len(sec_list):
        return False
    idx: int = 0
    while idx < len(first_list):
        if first_list[idx] != sec_list[idx]:
            return False
        idx += 1
    return True