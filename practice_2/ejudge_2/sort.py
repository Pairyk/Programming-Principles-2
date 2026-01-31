def main():
    _ = input()
    nums = list(map(int, input().split()))
    sorted_nums = sorted(nums, reverse=True)
    print(*sorted_nums)


if __name__ == "__main__":
    main()
