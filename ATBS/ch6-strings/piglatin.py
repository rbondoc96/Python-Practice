#!/usr/bin/env python


def eng_to_piglatin(word):
    VOWELS = ("a", "e", "i", "o", "u", "y")

    prefix_non_letters = ""
    # Separate non-letters at the start of the word
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        return prefix_non_letters

    # Separate non-letters at the end of the word
    suffix_non_letters = ""        
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    # Separate prefixed consonants
    prefix_cons = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_cons += word[0]
        word = word[1:]

    if prefix_cons != "":
        ret = word + prefix_cons + "ay"
    else:
        ret = word + "yay"

    if was_upper:
        return ret.upper()
    elif was_title:
        return ret.title()

    return ret


def main():
    print("Enter the English message to translate into Pig Latin")
    message = input()

    words = message.split()
    words = [eng_to_piglatin(word) for word in words]

    print(" ".join(words))


if __name__ == "__main__":
    main()