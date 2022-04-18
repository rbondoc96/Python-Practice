from ex49.sentence import Sentence

from typing import List, Tuple

# Type definitions
Word = Tuple[str, str]


class ParserError(Exception):
    pass


class Parser:


    def peek(self, words: List[Word]) -> str:
        """Returns the type of the first Word in the list."""
        return words[0][0] if words else None

    
    def match(self, words: List[Word], expecting: str) -> Word:
        """Removes the first Word in the list.
        Returns the Word if the expected type is correct."""
        if words:
            word = words.pop(0)
            return word if word[0] == expecting else None
        return None


    def skip(self, words, word_type):
        """If the first word in the list is of the given type, it
        is removed from the list."""
        while self.peek(words) == word_type:
            self.match(words, word_type)


    def parse_verb(self, words):
        self.skip(words, "stop")

        if self.peek(words) == "verb":
            return self.match(words, "verb")
        else:
            raise ParserError("Expected a verb next.")


    def parse_object(self, words):
        self.skip(words, "stop")
        next_word = self.peek(words)

        if next_word == "noun":
            return self.match(words, "noun")
        elif next_word == "direction":
            return self.match(words, "direction")
        else:
            raise ParserError("Expected a noun or direction next.")


    def parse_subject(self, words):
        self.skip(words, "stop")
        next_word = self.peek(words)

        if next_word == "noun":
            return self.match(words, "noun")
        elif next_word == "verb":
            return ("noun", "player")
        else:
            raise ParserError("Expected a verb next.")


    def parse_sentence(self, words: List[Word]) -> Sentence:
        _subject = self.parse_subject(words)
        _verb = self.parse_verb(words)
        _object = self.parse_object(words)

        return Sentence(_subject[1], _verb[1], _object[1])