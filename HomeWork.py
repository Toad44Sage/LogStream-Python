"Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237."

input_user = input("Введите элементы списка через запятую. Вводить только числа:")
number_list = input_user.split(",")
for item in number_list:
    try:
        item = int(item)
        if item % 2 == 0:
            print(item)
        elif item == 237:
            break
    except ValueError:
        print(f"Ошибка: {item} не является числом!")