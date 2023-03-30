"""Dictionary Functions."""

__author__ = "730525708"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert1() -> None:
    """Testing invert with an empty dictionary."""
    assert invert({}) == {}


def test_invert2() -> None:
    """Testing invert with normal dictionary."""
    assert invert({'A': 'Gary', 'B': 'Shawn'}) == {"Gary": "A", "Shawn": "B"}


def test_invert3() -> None:
    """Testing invert two of the same keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color1() -> None:
    """Testing favorite color with an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color2() -> None:
    """Testing favorite color with a normal dictionary."""
    assert favorite_color({'Gary': 'Green', 'Shawn': 'Blue', 'Dude': 'Pink', 'Oppa': 'Pink'}) == "Pink"


def test_favorite_color3() -> None:
    """Testing favorite color with a tie."""
    assert favorite_color({'Dude': 'Pink', 'Gary': 'Pink', 'Bob': 'Green', 'Sponge': 'Green'}) == "Pink"


def test_count1() -> None:
    """Testing count with an empty list."""
    assert count([]) == {}


def test_count2() -> None:
    """Testing count with a normal list."""
    assert count(['ice', 'cold', 'ice', 'cold', 'cold', 'ice']) == {'ice': 3, 'cold': 3}


def test_count3() -> None:
    """Testing count with an item not found in list."""
    assert count(['ice', 'ice', 'cold', 'cold', 'shower']) == {'ice': 2, 'cold': 2, 'shower': 1}