import re

text = input()

hell = re.search(r"dog|cat", text)

print("Yes" if hell else "No")