import re

text = input()

matched = re.match(r"^\w+\d+$", text)

print("Yes" if matched else "No")