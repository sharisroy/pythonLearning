item = {'name': 'Haris', 'age': 30}
print(item)
print(item['name'])
print(item['age'])

# Adding New Key-Value Pairs

item['phone'] = '01722906025'
print(item)
print(item['name'])
print(item['age'])
print(item['phone'])

# Modifying Values in a Dictionary

item['name'] = 'Haris Chandra Roy'
print(item)
print(item['name'])

# Removing Key-Value Pairs

del item['age']
print(item)