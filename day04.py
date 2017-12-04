"""
http://adventofcode.com/2017/day/4
"""

import pytest


def is_valid(passphrase):
    words = passphrase.split()
    unique_words = set(words)
    return len(unique_words) == len(words)

@pytest.mark.parametrize("phrase, valid", [
    ("aa bb cc dd ee", True),
    ("aa bb cc dd aa", False),
    ("aa bb cc dd aaa", True),
])
def test_is_valid(phrase, valid):
    assert is_valid(phrase) == valid


if __name__ == '__main__':
    with open("day04_input.txt") as finput:
        num_valid = sum(int(is_valid(line)) for line in finput)

    print(f"Part 1: there are {num_valid} valid passphrases")
