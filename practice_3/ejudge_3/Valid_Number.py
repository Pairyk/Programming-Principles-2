def main():
    num = input()
    print("Valid" if not set(num) & set("13579") else "Not valid")

if __name__ == "__main__":
    main()