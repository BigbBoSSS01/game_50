# запрашиваем у пользователя день и месяц роождения
counter = int(input('enter counter: '))

while True :

    birth_day = int(input("Введите день рождения:{counter} "))
    birth_month = int(input("Введите месяц рождения: "))
    if  birth_day == 'stop':
        print('finish')
        break
    if birth_month == 'stop':
        print('finish')
        break

    # а тут мы уже пишем очень длинный и нудный код

    if birth_month == 1:
        if birth_day >= 20:
            zodiac_sign = "Водолей"
        else:
            zodiac_sign = "Козерог"
    elif birth_month == 2:
        if birth_day >= 19:
            zodiac_sign = "Рыбы"
        else:
            zodiac_sign = "Водолей"
    elif birth_month == 3:
        if birth_day >= 21:
            zodiac_sign = "Овен"
        else:
            zodiac_sign = "Рыбы"
    elif birth_month == 4:
        if birth_day >= 20:
            zodiac_sign = "Телец"
        else:
            zodiac_sign = "Овен"
    elif birth_month == 5:
        if birth_day >= 21:
            zodiac_sign = "Близнецы"
        else:
            zodiac_sign = "Телец"
    elif birth_month == 6:
        if birth_day >= 21:
            zodiac_sign = "Рак"
        else:
            zodiac_sign = "Близнецы"
    elif birth_month == 7:
        if birth_day >= 23:
            zodiac_sign = "Лев"
        else:
            zodiac_sign = "Рак"
    elif birth_month == 8:
        if birth_day >= 23:
            zodiac_sign = "Дева"
        else:
            zodiac_sign = "Лев"
    elif birth_month == 9:
        if birth_day >= 23:
            zodiac_sign = "Весы"
        else:
            zodiac_sign = "Дева"
    elif birth_month == 10:
        if birth_day >= 23:
            zodiac_sign = "Скорпион"
        else:
            zodiac_sign = "Весы"
    elif birth_month == 11:
        if birth_day >= 22:
            zodiac_sign = "Стрелец"
        else:
            zodiac_sign = "Скорпион"
    elif birth_month == 12:
        if birth_day >= 22:
            zodiac_sign = "Козерог"
        else:
            zodiac_sign = "Стрелец"
    else:
        print("Неправильный месяц.")
        exit()

    print("Ваш знак зодиака: " + zodiac_sign)