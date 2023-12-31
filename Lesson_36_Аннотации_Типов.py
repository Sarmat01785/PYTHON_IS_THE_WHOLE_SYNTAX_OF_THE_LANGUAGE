# Аннотации Типов
"""
Аннотации типов в Python - это способ указать ожидаемые типы аргументов функции 
и тип возвращаемого значения. Хотя Python является динамически типизированным языком, 
использование аннотаций типов может помочь в понимании ожидаемых типов данных и улучшить читаемость кода.
"""


# Для примера, давай создадим функцию, которая принимает два числа и 
# возвращает их сумму, а затем добавим аннотации типов:
def add_numbers(a: int, b: int) -> int:
    return a + b
"""
В этом примере мы указали, что аргументы a и b должны быть целыми числами (int), 
а функция будет возвращать целое число (int).
"""



# Еще один пример можно привести для работы со списками. Допустим,
# у нас есть функция, которая принимает список целых чисел 
# и возвращает их сумму:
from typing import List

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)
"""
Здесь мы использовали аннотацию List[int] для указания, 
что ожидается список целых чисел, а функция вернет целое число.

Обрати внимание, что аннотации типов не влияют на фактическое выполнение кода, 
они используются только для подсказок и проверок типов статическим анализатором 
кода или инструментами разработки.
"""