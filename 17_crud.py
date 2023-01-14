# CRUD -> por sus siglas en ingles: 'Crear', 'Leer', 'Actualizar' y 'Borrar'. CREATE READ UPDATE & DELETE.

numbers = [1, 2, 3, 4, 5]  # Lista
# print(numbers[1])  # ir sobre un elemento determinado
numbers[-1] = 10  # Para actualizar un elemento en la lista
print(numbers)
numbers.append(700)
print(numbers)

numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

task = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + task
print(new_list)
# print(new_list.index('todo 2'))

# Index

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

# Pop

new_list.pop(0)
print(new_list)

# Reverse

new_list.reverse()
print(new_list)

# Sort

numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)



