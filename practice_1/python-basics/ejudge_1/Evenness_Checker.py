"""
Problem 118: 503043. Evenness Checker
Read an integer and check if it is even or odd.
"""


def main():
    a = int(input())

    print("even" if a % 2 == 0 else "odd")


if __name__ == "__main__":
    main()
