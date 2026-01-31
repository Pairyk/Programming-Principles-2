from collections import Counter


def main():
    _ = input()
    nums = list(map(int, input().split()))

    freq = Counter(nums)
    max_freq = max(freq.values())
    max_num = min(num for num, count in freq.items() if count == max_freq)

    print(max_num)


if __name__ == "__main__":
    main()
