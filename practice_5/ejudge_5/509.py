import re

text = input()

help_me = re.findall(r"\b\w{3}\b", text)

print(len(help_me))