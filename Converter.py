# Калькулятор переводит заданные единицы измерения в СИ
quantity = int(input("Выберите физическую величину из списка: \n 1 : Время  \n 2 : Масса \n 3 : Температура \n"))
# Перевод времени в секунды
if quantity == 1:
    time_type = int(input("Выберите тип операции: \n 1 : дни -> сек \n 2 : часы -> сек \n 3: минуты -> сек \n"))
    time = float(input("Введите значение: \n"))
    if time_type == 1:
        print("Время в секундах:", time * 86400)
    elif time_type == 2:
        print("Время в секундах:", time * 60 * 60)
    elif time_type == 3:
        print("Время в секундах:", time * 60)
# Перевод массы в килограммы
elif quantity == 2:
    weight_type = int(input("Выберите тип операции: \n 1 : Тонны -> кг \n 2 : Центнеры -> кг \n 3 : Граммы -> кг \n"))
    weight = float(input("Введите значение: \n"))
    if weight_type == 1:
        print("Масса в килограммах:", weight * 1000)
    elif weight_type == 2:
        print("Масса в килограммах:", weight * 100)
    elif weight_type == 3:
        print("Масса в килограммах:", weight / 1000)
# Перевод температуры в градусы Цельсия или Кельвина
elif quantity == 3:
    temp_type = int(input("Выберите тип операции: "
                          "\n 1 : Фаренгейт -> Цельсия"
                          "\n 2 : Фаренгейт -> Кельвин \n 3: Цельсия -> Кельвин \n 4 : Кельвин -> Цельсия"))
    temp = float(input("Введите значение: \n"))
    if temp_type == 1:
        print("Температура по Цельсия:", (temp - 32) * 5 / 9)
    elif temp_type == 2:
        print("Температура по Кельвину", ((temp - 32) * 5 / 9) + 273.15)
    elif temp_type == 3:
        print("Температура по Кельвину", temp + 273.15)
    elif temp_type == 4:
        print("Температура по Кельвину", temp - 273.15)
else:
    print("Введенные значения не верны")
