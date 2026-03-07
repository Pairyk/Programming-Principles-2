import re

text = input()

help = re.findall(r"[A-Z]", text)
print(len(help))