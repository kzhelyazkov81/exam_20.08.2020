import re
data = input()
regex = r'(\#|\|)(?P<name>[A-Z a-z]+)\1(?P<date>[0-3][0-9]/[0-1][0-9]/\d{2})\1(?P<calories>(?:[1-9]\d{0,3})|(?:10000))\1'
matches = re.finditer(regex, data)
total_calories = 0
items = {}
n=1
for match in matches:
    name = match.group('name')
    date = match.group('date')
    calories = int(match.group('calories'))
    items[n] = {}
    items[n]["name"] = name
    items[n]['date'] = date
    items[n]['calories'] = calories
    total_calories += calories
    n += 1

days = total_calories // 2000
print(f'You have food to last you for: {days} days!')
for n in items:
    item_name = items[n]['name']
    expiration_date = items[n]['date']
    calories = items[n]['calories']
    print(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')
