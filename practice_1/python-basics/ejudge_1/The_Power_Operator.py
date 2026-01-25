"""
Problem 106: 503031. The Power Operator
Read integers a and b and calculate a raised to the power of b.
"""


def powerer(number, power) -> None:
    print(number**power)


def main():
    number = int(input())
    power = int(input())

    powerer(number, power)


if __name__ == "__main__":
    main()
