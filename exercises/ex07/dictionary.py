"""Dictionary Functions."""

__author__ = "730525708"


def invert(dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of a dictionary."""
    dict_invert = {}
    for key in dict:
        if dict[key] in dict_invert:
            raise KeyError(f"KeyError: '{dict[key]}' already exists.")
        dict_invert[dict[key]] = key
    return dict_invert


def favorite_color(fav_color_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently.."""
    result: dict[str, int] = {}
    most_frequent: str = ""
    for names in fav_color_dict:
        color = fav_color_dict[names]
        if color in result:
            result[color] += 1
        else:
            result[color] = 1
    max_frequent: int = 0
    for colors in result:
        if result[colors] > max_frequent:
            max_frequent = result[colors]
            most_frequent = colors
    return most_frequent


def count(count_list: list[str]) -> dict[str, int]:
    """Returns unique keys in the given list and each value is associated with count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in count_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result