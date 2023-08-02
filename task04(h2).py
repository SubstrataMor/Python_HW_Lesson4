# задача 2 необязательная.
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re


# Еще не доделал, код не работает

import re


def sum_polynomials(poly1: str, poly2: str) -> str:
    terms1 = re.findall(r'([+-]?\d)x^(\d+)', poly1)
    terms2 = re.findall(r'([+-]?\d)x^(\d+)', poly2)

    combined_terms = {}
    for coefficient, exponent in terms1:
        combined_terms[int(exponent)] = combined_terms.get(
            int(exponent), 0) + int(coefficient)
    for coefficient, exponent in terms2:
        combined_terms[int(exponent)] = combined_terms.get(
            int(exponent), 0) + int(coefficient)

    result = ''
    for exponent, coefficient in combined_terms.items():
        result += f'{coefficient:+d}x^{exponent}'

    return result


poly1 = input("Введите первый многочлен: ")
poly2 = input("Введите второй многочлен: ")
result = sum_polynomials(poly1, poly2)
print(f"Результат: {result}")

# х5 – х4 – 5х3 + х2 + 8х + 4 = 0
# 4x3 + 6x2 + 4х + 1 = 0
