import re

text = input()

lol = re.findall(r"\d{2,}", text)

print(*lol, sep=" ")