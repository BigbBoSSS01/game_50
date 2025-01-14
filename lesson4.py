#  Структуры данных: списки - list, срезы, кортежи - tuple.
# sum, min, max, len

# expenses = [int(input(f'введите расход за день: {i}) ')) for i in range(1, 8)]
# print(sum(expenses) / len(expenses))

# number = (4,)
# print(number)
# print(type(number))

# cities = ('tokmok', 'bishkek', 'osh', 'kara-balta')
# cities = list(cities)
# print(cities)

# print(cities[-1])
# print(cities[::2])
# print(type(cities))




"""list"""
# numbers = [4, 2, 7.3, 5.8, 1, 6, 99]

# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# print(len(numbers))

"""что может делать встроенная функция list()"""
# print(list('geeks'))
# print(list(range(1, 11)))

# students = ['ilziya', 'ayana', 'ibragim', 'dmitriy', 'syimyk']
# print(students[2:-1])

"""list comprehension"""
# students = [student.upper() for student in students if student.startswith('i')]
# students = [student.upper() for student in students if student.startswith('i')]
# print(students)

# students2 = ['bekbol', 'bekzat']
# print(students)

"""удалить"""
# del students[:3]
# students.remove('ibragim')
# deleted = students.pop(2)
# print(deleted)

"""изменение"""
# students.reverse()
# students.sort(reverse=True)
# students[1] = 'aiana'
# students[0], students[1] = students[1], students[0]
# students[:2] = students2

"""добавление"""
# students.append('bekbolsun')
# students.insert(1, 'ruslan')
# students.extend(students2)

"""как обращаться по индексам и срезам"""
# print(students[1])
# print(students[2::])
# print(students[2::])

