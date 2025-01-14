def nearest_number(numbers, target):
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    return target, sorted_numbers

def get_element_at_index(iterable):
    while True:
        try:
            index = int(input("Введите индекс элемента: "))
            element = iterable[index]
            print(f"Элемент с индексом {index}: {element}")
        except IndexError:
            print(f"Индекс {index} выходит за пределы допустимого диапазона (от 0 до {len(iterable) - 1})")
        except ValueError:
            print("Пожалуйста, введите целочисленный индекс.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            continue


result1 = nearest_number([312, 996, 31, 1991], 1000)
print(result1)  

result2 = nearest_number([5, 20.18, 103, 4], 27)
print(result2)  


my_list = [10, 20, 30, 40, 50]
get_element_at_index(my_list)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)  

mapped_numbers = list(map(lambda x: x * 2, numbers))
print(mapped_numbers)  