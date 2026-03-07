import re

with open('raw') as file:
    data = file.read()

all_prices = re.findall(r"\d+\s?\d*,00", data)

all_names = re.findall(r"\d+\.\n(.+)", data)
amount_of_products = len(all_names)

date_and_time = re.findall(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", data)

all_prices = set(all_prices)

for i, price in enumerate(all_prices):
    print(f"{i+1}. {price}")

for i, name in enumerate(all_names):
    print(f"{i+1}. {name}")

print(f"\nThe total amount of products: {amount_of_products}")
print(f"\nDate and time: {date_and_time}")