import pytest
from main import Word, Sentence, Text, Program


def test_word_equality():
    w1 = Word("Hello")
    w2 = Word("hello")

    assert w1 == w2


def test_sentence_word_set():
    s = Sentence("Hello world hello")

    word_set = s.get_word_set()

    assert len(word_set) == 2


def test_text_parsing():
    text = Text("Hello world! Hi there.")

    assert len(text.sentences) == 2


def test_normalize_text():
    text = "Hello   world"
    result = Program.normalize_text(text)

    assert result == "Hello world"


def test_find_max_sentences():
    text = Text("Hello world! World hello. Hi there.")

    result = Program.find_max_sentences(text)

    assert len(result) == 2
    assert str(result[0]) in ["Hello world", "World hello"]


def test_find_empty_text():
    text = Text("")

    result = Program.find_max_sentences(text)

    assert result == []
