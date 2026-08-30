from pipeline import (
    clean_spaces,
    lowercase,
    remove_special_chars,
    remove_stopwords,
    word_frequency,
    run_pipeline,
)


def main() -> None:

    text = "  HELLO!!! I am learning Python.   "

    pipeline = [
        clean_spaces,
        lowercase,
        remove_special_chars,
        remove_stopwords,
        word_frequency,
    ]

    result = run_pipeline(text, pipeline)

    print("Input:")
    print(text)

    print("\nOutput:")
    print(result)


if __name__ == "__main__":
    main()