import re

text = input()
lmao = re.findall("\w+", text)
print(len(lmao))