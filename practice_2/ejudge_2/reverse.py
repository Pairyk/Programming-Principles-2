def main():
    _, l, r = map(int, input().split())
    nums = list(map(int, input().split()))

    nums[l - 1 : r] = nums[l - 1 : r][::-1]

    print(*nums)


if __name__ == "__main__":
    main()
