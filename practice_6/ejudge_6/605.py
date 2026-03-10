word = input().lower()

print("Yes" if any(l in ('a','e','i','o','u') for l in word) else "No")