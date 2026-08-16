from utils import char_dicts, char_dict_to_sort_list


def get_num_words(texts: str) -> int:
    word_count = len(texts.split())
    return word_count


def get_char_count(texts: str) -> int:
    characters = char_dicts(texts)
    char_count = char_dict_to_sort_list(characters)
    return char_count
