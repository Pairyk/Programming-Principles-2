import re

text = input()
splitter = input()

arr = re.split(r""+ splitter, text)

print(*arr, sep=",")