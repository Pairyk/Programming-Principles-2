import re

text = input()
new_text = re.findall(r"\w+: ([^,|\n]+)", text)
print(*new_text)