# Конспект: Словари, методы dict()
# Часть 2. Итерация

"""
Словари в Python предоставляют ряд методов для итерации и управления данными.
Итерация по словарю может выполняться по ключам, значениям или парам ключ-значение.
"""

# Создание словаря
student = {
    "имя": "Анна",
    "возраст": 20,
    "курс": "Программирование"
}

# Получение количества элементов в словаре
print(len(student))  # Выводит 3

# Получение значения по ключу с помощью метода get()
age = student.get("возраст")
print(age)  # Выводит 20

# Удаление элемента по ключу с помощью метода pop()
course = student.pop("курс")
print(course)  # Выводит "Программирование"

# Перебор всех ключей словаря
for key in student:
    print(key)

# Перебор всех значений словаря
for value in student.values():
    print(value)

# Перебор всех пар ключ-значение словаря
for key, value in student.items():
    print(f"{key}: {value}")

# Итерация по словарю с изменением значений
price = {"мясо": 3, "хлеб": 1, "картошка": 0.5, "вода": 0.2}
for item in price:
    price[item] *= 0.85  # Применяется скидка в 15%
print(price)  # Выводит обновленные цены

# Создание нового словаря на основе старого с изменением значений
new_price = {item: round(value * 0.85, 2) for item, value in price.items()}
print(new_price)  # Выводит новый словарь со скидкой

# Извлечение представления значений из словаря
values_view = price.values()
print(list(values_view))  # Преобразуем представление в список значений

# Инверсия словаря (ключи становятся значениями и наоборот)
inverted_price = {value: key for key, value in price.items()}
print(inverted_price)  # Выводит инвертированный словарь

# Исходный код с использованием метода keys() для итерации по ключам словаря
price = {"мясо": 3, "хлеб": 1, "картошка": 0.5, "вода": 0.2}
for k in price.keys():
    print(k)  # Выводит все ключи словаря
    # мясо
    # хлеб
    # картошка
    # вода

# Улучшенный код для итерации по ключам словаря
price = {"мясо": 3, "хлеб": 1, "картошка": 0.5, "вода": 0.2}
for k in price:
    print(k)  # Выводит все ключи словаря
    # мясо
    # хлеб
    # картошка
    # вода
