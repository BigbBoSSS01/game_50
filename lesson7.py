# lambda , функция работа с исключениями

# def up_letter(worb: str) -> str:
#     return worb.title()



# def show_words(func, objects):
#     for i in objects:
#         print(func(i))

# show_words(lambda word: word.title(), objects:['kemin','karakol','osh'])


# words = ['tokmok', 'karakol','kant']
# # show_words(up_letter, word
# sorte_words =sorted(words, key=lambda word: word[-1])
# filter_words = list(filter(lambda word: '-' not in word, words))
# map_word = tuple(map(lambda word: word.upper(), words))

# print(sorte_words, filter_words,  map_word, sep='\n')
# words = [i.upper() for i in words if '-' not in i]
# print(words)


""""lambda"""

# lambda_f = lambda num1, num2 : num1 + num2

# print(lambda_f(2, 4))


# names = ['azamat', 'erlan','samat','uluk']
# print(names)

# sorted_names = sorted(names, key=lambda x: x[1])
# print(sorted_names)

# filtered_names = list(filter(lambda n: len(n) == 5, names))
# print(filtered_names)

# mapped_names = list(map(lambda n: n.upper(), names))
# print(mapped_names)



# numbers = [398,34,32323,33]

# mapped_numbers = list(map(lambda n: n*2, numbers ))
# print(mapped_numbers)

# filered = list(filter(lambda n : 100 < n >60, numbers))
# print(filered)


# Работа с исключениями''''''""""""""

# try:
#     print(2 * 'py')
# except:
#     print('нашли ошибку')
# else:
#     print('проверка прошла успешна')
# finally:
#     print('проверка завершена')


word = input('введите слово: ')
data = {}

while True:
    print(data)
    index_in = input('напиши любую цифру или же букву "q" чтобы выключить программу ')
    if index_in == 'q':
        break
    else:
        try:
            index_in = int(index_in)
            data[index_in] = word[index_in]
            print(word[index_in])
        except IndexError:
            print(f'вводите только числа от 0 до {len(word)-1}')
        except ValueError:
            print('нельзя вводить буквы')




