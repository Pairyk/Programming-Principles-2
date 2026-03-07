import re 

text = input()
matched = re.match(r"^Hello", text)

print("Yes" if matched else "No")