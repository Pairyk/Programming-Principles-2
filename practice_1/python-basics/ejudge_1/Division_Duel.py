"""
Problem 105: 503030. Division Duel
In Python, / and // do different things. Read two integers a and b,
and output the result of float division followed by integer division.
"""


def duel(a, b) -> None:
    print(a // b)
    print(a / b)


def main():
    a = int(input())
    b = int(input())

    duel(a, b)


if __name__ == "__main__":
    main()
