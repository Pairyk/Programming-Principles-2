import re

text = input()
subtext = input()
replace = input()

new_text = re.sub(subtext, replace, text)

print(new_text)