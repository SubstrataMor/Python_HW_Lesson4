# задача 1 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, 
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

# 160 / 8 = 20 | 0 
#  20 / 8 =  2 | 4
#   2 / 8 =  0 | 2

# 18 / 2 = 9 | 0
#  9 / 2 = 4 | 1
#  4 / 2 = 2 | 0
#  2 / 2 = 1 | 0
#  1 / 2 = 0 | 1

def transfomation(num: int) ->str:
    binary = ""
    octal=""
    num_bin = num
    num_oct = num
    while num_bin > 0:
        binary=str(num_bin%2)+binary
        num_bin//=2
    while num_oct >0:
        octal=str(num_oct%8)+octal
        num_oct//=8
    return f"Двоичное: 0b{binary}, Восьмиричное: 0o{octal}"

number = int(input("Введите число: "))
result = transfomation(number)
print(result)
print(bin(number), oct(number))