def get_num_words(texts):
    word_count = len(texts.split())
    return word_count


def get_char_count(texts):
    chars_count = {}
    for word in texts:
        split_word = word.split()
        for char in split_word:
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1

    char_count = sum(chars_count.values())
    return char_count
