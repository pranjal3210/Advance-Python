from pipeline import (
    clean_spaces,
    lowercase,
    remove_special_chars,
    remove_stopwords,
    word_frequency,
    run_pipeline,
)


def test_clean_spaces():
    text = "  hello    python   "

    assert clean_spaces(text) == "hello python"


def test_lowercase():
    assert lowercase("HELLO") == "hello"


def test_remove_special_chars():
    assert remove_special_chars("hello!!!") == "hello"


def test_remove_stopwords():
    text = "hello i am learning"

    result = remove_stopwords(text)

    assert result == "hello learning"


def test_word_frequency():
    text = "python python ai"

    result = word_frequency(text)

    assert result == {
        "python": 2,
        "ai": 1,
    }


def test_pipeline():

    text = "  HELLO!!! I am learning Python.   "

    pipeline = [
        clean_spaces,
        lowercase,
        remove_special_chars,
        remove_stopwords,
        word_frequency,
    ]

    result = run_pipeline(text, pipeline)

    assert result == {
        "hello": 1,
        "learning": 1,
        "python": 1,
    }