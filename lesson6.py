"""Функции :виды параметроов возвращение данных виды аоргументов """
"""определение наименование (параметры):
    тело функции
    возвращение обьекта (результат)
    
    
вызов функции 
наиименование функции(аргументы)"""


# def some_function(name, surname='неизвестно'):
#     print(f'name: {name} surname: {surname}')


# some_function('stalker', 'sdhb')
# some_function(surname='debil', name='gerry')
# some_function('stalker')




"""возвращение - retern"""
# def get_square(lenght: int, width: int) -> int:
#     """принимает длину,ширину и возвращает площадь"""
#     square = lenght * width
#     return square


# print(help(get_square))
# print(get_square.__doc__)
# print(get_square.__annotations__)



# square_2 = get_square(7,5)
# square_victory = get_square(width=110, lenght=350)
# square_hall = get_square(lenght=int(input('веедите длину:')),width=int(input('введите ширину:')))

# print(square_2, square_victory,square_hall, sep='\n')




"""*args and **kwargs"""

# def menu(**kwargs):
#     return kwargs
# monday = menu(eat='sjdjs', drink='alkogol', sd=899)
# print(monday)


# def plus(*args):
#     return sum(args)
# print(plus(23,2,32,3,32,3,23,))
# print(plus(232,2,3,23,2,3,23,23,23,))


# def max1(obj):

def max(*args, key=None):
    if len(args) == 1 and hasattr(args[0], 'iter'):
        # Если передан один итерируемый объект (например, список)
        iterable = args[0]
    else:
        # Если передано несколько отдельных значений
        iterable = args

    largest = None
    for item in iterable:
        if largest is None or (key(item) if key else item) > (key(largest) if key else largest):
            largest = item
    return largest


print(max([1,1,1,1,8]))