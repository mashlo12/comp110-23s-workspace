def odd_and_even(list_1: list[int]) -> list[int]:
    idx: int = 0
    new_list: list[int] = []
    while idx < len(list_1):
        if list_1[idx] % 2 == 1 and idx % 2 == 0:
            new_list.append(list_1[idx])
            idx += 1

    return new_list


def value_exists(inp_dict: dict[str, int], val: int) -> bool:
    exists: bool = False
    for elem in inp_dict:
        if
