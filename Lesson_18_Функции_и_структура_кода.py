# Конспект: Функции и структура кода

# Передача значений между функциями
"""
Передача значений между функциями в Python позволяет использовать результаты
выполнения одной функции в другой функции. Это упрощает структурирование кода и его организацию.
"""


# Функция, возвращающая квадрат числа
def square(number):
    return number ** 2  # Возврат квадрата аргумента


# Функция, вычисляющая сумму двух чисел
def calculate_sum(a, b):
    return a + b  # Возврат суммы аргументов


# Вызов функции square и передача результата в calculate_sum
result = square(5)  # Результат вызова square с аргументом 5
final_result = calculate_sum(result, 10)  # Результат вызова calculate_sum с результатом square и числом 10

# Вывод итогового результата
print(final_result)  # Выводит 35

'''
Функция square принимает число, возводит его в квадрат и возвращает результат.
Функция calculate_sum принимает два числа и возвращает их сумму.
В основной части кода мы вызываем square с аргументом 5 и передаем результат в calculate_sum,
где он суммируется с 10, и выводим полученное значение.
'''

# Пример кода для вычисления объема цилиндра

# Импорт модуля math для доступа к математическим функциям и константам
import math

# Присвоение переменной PI значения числа пи из модуля math
PI = math.pi


# Функция для вычисления радиуса цилиндра
def radius():
    n = float(input("Введите диаметр цилиндра в см: "))  # Получение диаметра от пользователя и преобразование в float
    n /= 2  # Половина диаметра - это радиус
    return n  # Возврат значения радиуса


# Функция для вычисления высоты цилиндра
def height():
    m = float(input("Введите высоту цилиндра в см: "))  # Получение высоты от пользователя и преобразование в float
    return m  # Возврат значения высоты


# Функция для вычисления объема цилиндра
def volume():
    r = radius()  # Получение радиуса с помощью функции radius
    h = height()  # Получение высоты с помощью функции height
    s = PI * r ** 2  # Вычисление площади основания цилиндра
    v = s * h  # Вычисление объема цилиндра
    return v  # Возврат значения объема


# Вывод объема цилиндра
print("Объем цилиндра", volume(), "см3")  # Вызов функции volume и вывод результата

'''
В данном примере используются функции radius и height для запроса у пользователя размеров цилиндра,
а функция volume использует результаты этих функций для расчета и вывода объема цилиндра.
'''

import math


def radius():
    """Получает диаметр цилиндра от пользователя и возвращает радиус."""
    diameter = float(input("Введите диаметр цилиндра в см: "))
    return diameter / 2


def height():
    """Получает высоту цилиндра от пользователя и возвращает ее."""
    return float(input("Введите высоту цилиндра в см: "))


def volume(radius, height):
    """Вычисляет и возвращает объем цилиндра на основе радиуса и высоты."""
    base_area = math.pi * radius ** 2
    return base_area * height


def massa(volume, density):
    """Вычисляет и возвращает массу цилиндра на основе его объема и удельного веса."""
    return volume * density / 1000  # Переводим из грамм/см^3 в килограммы


# Получение данных от пользователя
r = radius()
h = height()
density = float(input("Введите удельный вес материала цилиндра в г/см3: "))

# Вычисление объема и массы
cylinder_volume = volume(r, h)
cylinder_mass = massa(cylinder_volume, density)

# Вывод результата
print(f"Объем цилиндра: {cylinder_volume:.2f} см3")
print(f"Вес цилиндра в кг: {cylinder_mass:.2f}")
