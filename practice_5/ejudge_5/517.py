import re

text = input()
new = re.findall(r"\d\d/\d\d/\d\d\d\d", text)
print(len(new))