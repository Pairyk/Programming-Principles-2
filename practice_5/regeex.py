import re

text = input()
new = re.sub(r"[A-Z]", lambda a: "_" + a.group().lower(), text)

print(new)