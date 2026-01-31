def main():
    _ = input()

    nums = list(map(int, input().split()))
    square = lambda a: a * a
    print(*[square(num) for num in nums])


if __name__ == "__main__":
    main()
