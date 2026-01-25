"""
Problem 119: 503044. Find and Replace
Read a sentence, a target word, and a replacement word.
Replace all occurrences of the target with the replacement.
"""


def main():
    sentence = input()
    target = input()
    replacement = input()

    print(sentence.replace(target, replacement))


if __name__ == "__main__":
    main()
