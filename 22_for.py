
'''
for element in range(1, 21):
  print(element)
'''
# ciclo for in listas
my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

# Ciclo for en tuples
my_tuple = ('Joaco', 'Mafe', 'Vicky')
for i in my_tuple:
  print(i)

# Ciclo for en diccionarios
product = {'name': 'camisa', 'price': 100, 'stock': 89}

for i in product:
  print(i, '--> ', product[i])

for key, value in product.items():
  print(key, '-->', value)

# Lista de diccionarios

people = [{
  'name': 'Joaco',
  'age': 33,
}, {
  'name': 'Mafe',
  'age': 23,
}, {
  'name': 'Isis',
  'age': 39
}]

for i in people:
  print(i)

for i in people:
  print('name --> ', i['name'])

for i in people:
  print('age --> ', i['age'])


