"""'list' Utility Functions."""
__author__ = "730525708"

from exercises.ex05.utils import only_evens

def test_only_evens_edge_case() -> None:
    """Test with empty list."""
    assert only_evens([]) == []

def test_only_evens_use_case_1() -> None:
    """Test with odd number."""
    assert only_evens([1, 3, 5]) == []

def test_only_evens_use_case_2() -> None:
    """Test with even and odd numbers."""
    assert only_evens([2, 3, 4, 5, 6]) == [2, 4, 6]


from exercises.ex05.utils import sub

def test_sub_edge_case() -> None:
    """Test with empty list."""
    assert sub([], 0, 0) == []

def test_sub_use_case_1() -> None:
    """Test with start index 0 and end index 4."""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]

def test_sub_use_case_2() -> None:
    """Test with start index 1 and end index 3"""
    assert sub([1, 2, 3, 4, 5, 6], 2, 4) == [3, 4]


from exercises.ex05.utils import concat

def test_concat_edge_case() -> None:
    """Test with empty list."""
    assert concat([], []) == []

def test_concat_use_case_1() -> None:
    """Test with non-empty list."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]

def test_concat_use_case_2() -> None:
    """Test with one empty list and one non-empty list."""
    assert concat([], [1, 2]) == [1, 2]


