import re

text = "apples banana,qiwi;lemon-melon-cookie"

fruits = re.split(r",|;| +", text)

print(fruits)