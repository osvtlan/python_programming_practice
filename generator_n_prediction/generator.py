from typing import Union
from io import StringIO


def matches(file: Union[str, StringIO], words: list):
    assert isinstance(words, list) and all(isinstance(word, str) for word in words)
    with open(file, "r", encoding="utf-8") if isinstance(file, str) else file as f:
        for line in f:
            elems = line.lower().split()
            if any(word.lower() in elems for word in words):
                yield line


if __name__ == '__main__':
    for match in matches("./text.txt", ["white", "принакрыл", "берёза", "Моим"]):
        print(match, end="")
