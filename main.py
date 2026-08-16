#!/usr/bin/env python3
from stats import get_num_words, get_char_count


def get_book_texts(book_name) -> str:
    with open(book_name) as f:
        book_texts = f.read()
        return book_texts


if __name__ == "__main__":
    book_name = "books/frankenstein.txt"
    book_texts = get_book_texts(book_name)
    word_count = get_num_words(book_texts)
    chars_count = get_char_count(book_texts)

    print(f"Found {word_count} total words in {book_name}")
    print(chars_count)
