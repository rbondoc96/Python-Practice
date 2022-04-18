import pytest

from ex49.parser import Parser, ParserError
from ex49.lexicon import Lexicon


@pytest.fixture
def lexicon():
    return Lexicon()

@pytest.fixture
def parser():
    return Parser()


def test_parser_1(lexicon, parser):
    words = lexicon.scan("The bear ate the princess")
    assert words == [
        ("stop", "The"),
        ("noun", "bear"),
        ("verb", "ate"),
        ("stop", "the"),
        ("noun", "princess"),
    ]
    sentence = parser.parse_sentence(words)

    assert sentence.subject == "bear"
    assert sentence.verb == "ate"
    assert sentence.object == "princess"


def test_parser_2(lexicon, parser):
    words = lexicon.scan("The bear eats honey")
    assert words == [
        ("stop", "The"),
        ("noun", "bear"),
        ("verb", "eats"),
        ("noun", "honey"),
    ]
    sentence = parser.parse_sentence(words)

    assert sentence.subject == "bear"
    assert sentence.verb == "eats"
    assert sentence.object == "honey"    


def test_parser_error_1(lexicon, parser):
    words = lexicon.scan("My name is Rodrigo")
    assert words == [
        ("error", "My"),
        ("error", "name"),
        ("error", "is"),
        ("error", "Rodrigo")
    ]

    try:
        sentence = parser.parse_sentence(words)
    except ParserError:
        assert True, "The lexicon should not understand the sentence."


def test_parser_error_2(lexicon, parser):
    words = lexicon.scan("The princess is Rodrigo")
    assert words == [
        ("stop", "The"),
        ("noun", "princess"),
        ("error", "is"),
        ("error", "Rodrigo")
    ]

    try:
        sentence = parser.parse_sentence(words)
    except ParserError:
        assert True, "The lexicon should not understand the sentence."

    