import re

text = input()
print(re.sub(r"\d", lambda a: a.group() * 2, text))