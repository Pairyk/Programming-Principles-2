def main():
    _ = input()
    nums = list(map(int, input().split()))
    max_num, min_num = max(nums), min(nums)

    result = [min_num if num == max_num else num for num in nums]
    print(*result)


if __name__ == "__main__":
    main()
