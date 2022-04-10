#!/usr/bin/env python3

import lib

def main():
    sentence = "All good things come to those who wait."
    words = lib.break_words(sentence)
    print(words)
    sorted_words = lib.sort_words(words)
    print(sorted_words)
    lib.print_first_word(words)
    lib.print_last_word(words)
    print(words)
    lib.print_first_word(sorted_words)
    lib.print_last_word(sorted_words)
    print(sorted_words)
    sorted_words = lib.sort_sentence(sentence)
    print(sorted_words)
    lib.print_first_and_last(sentence)
    lib.print_first_and_last_sorted(sentence)

if __name__ == "__main__":
    main()