import re

text = input()

subt = input()
patt = re.escape(subt)

new = re.findall(patt, text)
print(len(new))