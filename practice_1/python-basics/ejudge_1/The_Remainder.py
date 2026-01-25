"""
Problem 107: 503032. The Remainder
Read two integers a and b.
Calculate and print the remainder of the division of a by b .
"""


def remainder(a, b) -> None:
    print(a % b)


def main():
    a = int(input())
    b = int(input())

    remainder(a, b)


if __name__ == "__main__":
    main()
