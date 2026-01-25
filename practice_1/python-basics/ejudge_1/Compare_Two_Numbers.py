"""
Problem 120: 503045. Compare Two Numbers
Read two integers and compare them. Output the larger number.
If the numbers are equal, print “equal”.
"""


def compare(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "equal"


def main():
    a = int(input())
    b = int(input())

    print(compare(a, b))


if __name__ == "__main__":
    main()
