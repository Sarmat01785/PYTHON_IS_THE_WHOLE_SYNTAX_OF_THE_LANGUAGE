# Цикл for Часть 1.

"""
Цикл for используется для итерации по элементам последовательности, таких как список, строка или диапазон чисел.
"""

# Пример 1: Печать элементов списка
fruits = ["яблоко", "банан", "груша", "апельсин"]
for fruit in fruits:
    print(fruit)

# Пример 2: Подсчет суммы чисел в списке
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Сумма чисел:", total)

# Пример 3: Печать каждого символа в строке
message = "Привет, мир!"
for char in message:
    print(char)

# Пример 4: Использование оператора continue
# Оператор continue пропускает оставшуюся часть кода в текущей итерации и переходит к следующей итерации.
m = "String text"
for i in m:
    if i == "t":
        continue  # Пропускаем вывод и увеличение счетчика, если текущий символ 't'
    print(i)  # Этот код не выполнится, если предыдущее условие истинно

# После завершения цикла for, блок else выполняется, если цикл не был прерван оператором break.
else:
    print("Цикл завершен")

print("Программа работает дальше")
