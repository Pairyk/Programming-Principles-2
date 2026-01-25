"""
Problem 115: 503040. Membership Test
Read a long string and a short string.
Check if the short string is contained
within the long string and print the boolean result.
"""


def check(sentence, word) -> bool:
    return word in sentence


def main():
    sentence = input()
    word = input()
    print(check(sentence, word))


if __name__ == "__main__":
    main()
