def main():
    num = int(input())
    print(checker(num))


def checker(num):
    while num != 1:
        if num % 2 != 0:
            return "NO"
        num //= 2
    return "YES"


if __name__ == "__main__":
    main()
