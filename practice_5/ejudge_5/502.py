import re

text = input()
subtext = input()

matched = re.search(subtext, text)

print("Yes" if matched else "No")