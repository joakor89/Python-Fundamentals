
person = {
  'name': 'Joaquin',
  'last_name': 'Romero Flores',
  'langs': ['Python', 'R', 'SQL'],
  'age': 33,
}

print(person)

person['name'] = 'Andres'
person['age'] -= 5
person['langs'].append('rust')
print(person)

person['name'] = 'Joaquin Andres'
del person['last_name']
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
