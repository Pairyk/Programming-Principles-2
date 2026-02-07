def isUsual(num):
    if num <= 0:
        return False
    
    for prime in [2, 3, 5]:
        while num % prime == 0:
            num //= prime
    
    return num == 1


def main():
    n = int(input())
    print("Yes" if isUsual(n) else "No")


if __name__ == "__main__":
    main()