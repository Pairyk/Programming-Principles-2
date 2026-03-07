import re

text = input()

matched = re.findall(r"\d", text)

print(*matched, sep=' ')