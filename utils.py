def char_dicts(texts: str) -> dict[str, int]:
    char_counts = {}
    for word in texts:
        chars = word.split()
        for char in chars:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts


def char_dict_to_sort_list(dictionary: dict) -> list[tuple[str, int]]:
    result = sorted(list(dictionary.items()), key=lambda item: item[1], reverse=True)
    return result
