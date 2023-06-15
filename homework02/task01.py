# Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float) и
# возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения,
# вместо этого, необходимо повторно запросить у пользователя ввод данных.
def input_float():
    try:
        return float(input('Enter float number -> '))
    except ValueError:
        print('Invalid value, expected float number through dot("."): ')
        return input_float()


print(input_float())



