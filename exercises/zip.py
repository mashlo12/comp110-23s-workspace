def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    result_dict: dict[str, int] = {}
    if len(keys) != len(values):
        return result_dict
    for i in range(0, len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict