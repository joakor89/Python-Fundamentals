
my_dict = {}
print(type(my_dict))

my_dict = {
  'plane': 'aero-vehicle',
  'name': 'Joaquin',
  'last_name': 'Romero Flores',
  'age': 33
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))

print('plane' in my_dict)
print('avion' in my_dict)

