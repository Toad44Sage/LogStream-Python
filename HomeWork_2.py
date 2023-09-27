# Ввести произвольное число в консоле
# Ввести пограничное число в консоле
# Если 1-ое число меньше пограничного, вывести сообщение об этом.
# Если 1-ое число больше пограничного, вывести сообщение об этом.
# Если 1-ое число больше пограничного более, чем в 3 раза, сообщить об этом

input_user = input("Введите произвольное и пограничное число через пробел!:")
number_list = input_user.split()

if len(number_list) == 2:
    try:
        arbitrary_number = int(number_list[0])
        boundary_number = int(number_list[1])
        if arbitrary_number < boundary_number:
            print("Произвольное число меньше пограниченого...")
        elif arbitrary_number > boundary_number * 3:
            print("Произвольное число больше пограниченого более чем в три раза!!!")
        elif arbitrary_number > boundary_number:
            print("Произвольное число больше пограниченого!")
        elif arbitrary_number == boundary_number:
            print("Произвольное и пограниченое число равны 0_o")
    except ValueError:
        print("Ошибка: Вводить нужно только числа!")
else:
    print("Ошибка: Нужно ввести два числа!")


