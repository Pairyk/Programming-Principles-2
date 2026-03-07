import re

text = input()
matched = re.search(r"\S+@\S+\.\S+", text)

if matched:
    print(matched.group())
else:
    print("No email")