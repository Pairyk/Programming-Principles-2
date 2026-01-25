"""
Problem 102: 503024. Custom Separators
Read two strings and print them on a single line separated by three asterisks ***.
Use the sep parameter in the print() function.
"""


def main():
    word_1 = input()
    word_2 = input()
    print(word_1, word_2, sep="***")


if __name__ == "__main__":
    main()
