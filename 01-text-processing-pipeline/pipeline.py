import re
from collections.abc import Callable
from typing import Any


# -----------------------------
# 1. Clean spaces
# -----------------------------

def clean_spaces(text: str) -> str:
    """Remove extra spaces from text."""
    return " ".join(text.split())


# -----------------------------
# 2. Lowercase
# -----------------------------

def lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


# -----------------------------
# 3. Remove special characters
# -----------------------------

def remove_special_chars(text: str) -> str:
    """Remove punctuation and special characters."""

    return re.sub(r"[^a-zA-Z0-9\s]", "", text)


# -----------------------------
# 4. Remove stopwords
# -----------------------------

DEFAULT_STOPWORDS: set[str] = {
    "i",
    "am",
    "a",
    "an",
    "the",
    "is",
    "are",
    "and",
    "or",
    "to",
    "of",
    "in",
}


def remove_stopwords(
    text: str,
    *stopwords: str
) -> str:

    if not stopwords:
        stopwords = tuple(DEFAULT_STOPWORDS)

    words = text.split()

    filtered_words = filter(
        lambda word: word not in stopwords,
        words
    )

    return " ".join(filtered_words)


# -----------------------------
# 5. Word frequency
# -----------------------------

def word_frequency(text: str) -> dict[str, int]:
    """Count how many times each word appears."""

    words = text.split()

    frequency: dict[str, int] = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# -----------------------------
# 6. Run pipeline
# -----------------------------

def run_pipeline(
    text: str,
    pipeline: list[Callable[..., Any]],
    *args: Any,
    **kwargs: Any
) -> Any:

    result: Any = text

    for step in pipeline:
        result = step(result, *args, **kwargs)

    return result