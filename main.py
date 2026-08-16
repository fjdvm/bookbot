#!/usr/bin/env python3
from stats import get_num_words, get_char_count
import time


def get_book_texts(book_name) -> str:
    with open(book_name) as f:
        book_texts = f.read()
        return book_texts


def report(book_name: str, word_count: int, char_dicts: dict) -> str:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    time.sleep(3)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_dicts:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")


if __name__ == "__main__":
    book_name = "books/frankenstein.txt"
    book_texts = get_book_texts(book_name)
    word_count = get_num_words(book_texts)
    chars_count = get_char_count(book_texts)
    report(book_name, word_count, chars_count)
