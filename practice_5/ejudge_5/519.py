import re

text = input()
patt = re.compile(r"\b\w+\b")

new = patt.findall(text)

print(len(new))