import re

text = input()
lol_regex = re.compile(r"^\d+$")

print("Match" if lol_regex.search(text) else "No match")