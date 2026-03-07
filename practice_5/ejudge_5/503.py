import re

text = input()
subtext = input()

matched = re.findall(subtext, text)

print(len(matched))