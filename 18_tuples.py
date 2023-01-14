
numbers = (1, 2, 3, 5)
strings = ('Joaquin', 'Victoria', 'Nellys', 'Isis', 'Joaquin')
print(numbers)
print('0 --> ', numbers[0])
print('-1 --> ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD

# numbers.append(10)
# print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('Victoria'))
print(strings.count('Joaquin'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'Yael'
print(my_list)


my_tuple = tuple(my_list)
print(my_tuple)

