def full_name(firstName, middleName, lastName):
    if middleName:
        name = firstName + ' ' + middleName + ' ' + lastName
    else:
        name = firstName + ' ' + lastName
    return name


name = full_name('Haris', 'Chandra', 'Roy')
print(name)
name = full_name('Haris', '', 'Roy')
print(name)


# Passing a list
def full_name(item):
    for n in item:
        print("Hello Mr. " + n)


full_name(['Haris', 'Karim', 'Munna'])


# print item
def print_item(item):
    for value in item:
        print(value)
