# A Dictionary of Similar Objects
markOfStudents = {'Rahim': 87,
                  'Karim': 88,
                  'Munna': '89'
                  }

print("Karim's Mark is ", markOfStudents['Karim'],  ".")
print("Munna's Mark is " + markOfStudents['Munna'] + ".")

# Looping Through All Key-Value Pairs
name = {
    'firstName': 'Haris',
    'middleName': 'Chandra',
    'lastName': 'Roy'
}
for value in name.values():
    print('Value :' + value)

for key in name.keys():
    print('key :' + key)

for key, value in name.items():
    print('Key :' + key + '\tValue :' + value)

# Looping Through All Key-Value(Multiple) Pairs

favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

information = {
    'haris': ['Haris Chandra Roy', 30, 'DPL'],
    'rahim': ['Rahim Uddhin', '29', 'Pathao'],
    'karim': ['Karim Khan', '32', 'PP']
}

for key, info in information.items():
    print("\n" + key.title() + "'s Information is: ")
    print(info[2])
    for details in info:
        print("\t" + str(details))