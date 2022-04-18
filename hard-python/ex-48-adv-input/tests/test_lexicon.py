import pytest

from ex48.lexicon import Lexicon


@pytest.fixture(scope="module")
def lexicon():
    return Lexicon()


def test_directions(lexicon):
    assert lexicon.scan("north") == [("direction", "north")]
    result = lexicon.scan("north south east")
    assert result == [
        ("direction", "north"),
        ("direction", "south"),
        ("direction", "east"),
    ]


def test_verbs(lexicon):
    assert lexicon.scan("go") == [("verb", "go")]
    result = lexicon.scan("go kill eat")
    assert result == [
        ("verb", "go"),
        ("verb", "kill"),
        ("verb", "eat"),
    ]


def test_stops(lexicon):
    assert lexicon.scan("the") == [("stop", "the")]
    result = lexicon.scan("the in of")
    assert result == [
        ("stop", "the"),
        ("stop", "in"),
        ("stop", "of"),
    ]


def test_nouns(lexicon):
    assert lexicon.scan("bear") == [("noun", "bear")]
    result = lexicon.scan("bear princess")
    assert result == [
        ("noun", "bear"),
        ("noun", "princess"),
    ]


def test_numbers(lexicon):
    assert lexicon.scan("1234") == [("number", 1234)]
    result = lexicon.scan("3 91234")
    assert result == [
        ("number", 3),
        ("number", 91234)
    ]


def test_errors(lexicon):
    assert lexicon.scan("ASDFADFASDF") == [("error","ASDFADFASDF")]
    result = lexicon.scan("bear IAS princess")
    assert result == [
        ("noun", "bear"),
        ("error", "IAS"),
        ("noun", "princess"),
    ]


def test_capitalized_words(lexicon):
    assert lexicon.scan("Bear") == [("noun", "Bear")]
    assert lexicon.scan("PrinCeSS") == [("noun", "PrinCeSS")]
    result = lexicon.scan("the PRINCEss is IN BeAr")
    assert result == [
        ("stop", "the"),
        ("noun", "PRINCEss"),
        ("error", "is"),
        ("stop", "IN"),
        ("noun", "BeAr"),
    ]