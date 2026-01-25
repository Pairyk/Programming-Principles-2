"""
Problem 103: 503028. Int or String
Read one line. If it contains only digits, print “int”. Otherwise, print “str”.
"""


def main():
    object = input()

    if object.isdigit():
        print("int")
    else:
        print("str")


if __name__ == "__main__":
    main()
