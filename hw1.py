
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]

# expenses = []
# for day in days:
#     expense = input(f'потрачено {day}: ')
#     while not expense.replace('.', '', 1).isdigit():
#         print("вводите только числа")
#         expense = input(f'введите затраты  {day}: ')
#     expenses.append(float(expense))

# sum_of_expenses = sum(expenses)
# average_spending = round(sum_of_expenses / len(days), 1)

# print('затраты на неделю:', sum_of_expenses)
# print('дневные затраты:', average_spending)



# Monday = int(input('enter daily expenses for Monday:'))
# Tuesday = int(input('enter daily expenses for Tuesday:'))
# Wednesday = int(input('enter daily expenses for Wednesday:'))
# Thursday = int(input('enter daily expenses for Thursday:'))
# Friday = int(input('enter daily expenses for Friday:'))
# Saturday = int(input('enter daily expenses for Saturday:'))
# Sunday = int(input('enter daily expenses for Sunday:'))

# sum_of_expenses = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday

# days = 7
# average_spending = sum_of_expenses / days
# average_spending = round(average_spending, 1)
# print('сумма трат за неделю', sum_of_expenses)
# print('средний расход за день', average_spending)





gs = ['bish','osh', 'kb','bish 9']

gs = gs[::-1]
print(gs)
