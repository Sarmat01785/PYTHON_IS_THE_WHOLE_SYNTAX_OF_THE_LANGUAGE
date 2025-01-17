# Конспект: Словари, тип данных dict() в Python
# Часть 1. Варианты и методы

"""
Словари в Python - это структуры данных, которые хранят пары ключ-значение.
Они позволяют быстро получать доступ к данным по ключу и поддерживают различные методы для управления содержимым.
"""

# Создание словаря с использованием литерала
student = {
    "имя": "Анна",
    "возраст": 20,
    "курс": "Программирование"
}

# Доступ к элементам словаря по ключу
print(student["имя"])  # Выводит "Анна"
print(student["возраст"])  # Выводит 20

# Изменение значения элемента словаря
student["курс"] = "Искусственный интеллект"

# Добавление новой пары ключ-значение в словарь
student["группа"] = "A-32"

# Удаление элемента из словаря по ключу
del student["возраст"]

# Проверка наличия ключа в словаре
if "курс" in student:
    print("Ключ 'курс' присутствует в словаре")

# Получение списка ключей словаря
keys = student.keys()

# Получение списка значений словаря
values = student.values()

# Перебор всех пар ключ-значение в словаре
for key, value in student.items():
    print(key, ":", value)

# Создание словаря с помощью конструктора dict()
d1 = {"a": 7}
d2 = dict(a=7)

# Изменение и добавление элементов в словарь
d1["b"] = 9
d1["a"] = 8

# Вывод содержимого словарей
print(d1)  # Выводит {'a': 8, 'b': 9}
print(d2)  # Выводит {'a': 7}

# Удаление элемента из словаря d1
del d1["a"]
print(d1)  # Выводит {'b': 9}

# Создание словаря с ключами из списка и значением по умолчанию None
d3 = dict.fromkeys([1, 2, 3, 4, 5])
print(d3)  # Выводит {1: None, 2: None, 3: None, 4: None, 5: None}

# Создание словаря с ключами из списка и заданным значением по умолчанию
d3 = dict.fromkeys([1, 2, 3, 4, 5], "value")
print(d3)  # Выводит {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value'}


# Пример функции для покупки товаров
def buy():
    pay = 0
    while True:
        enter = input('Что покупаем???\n')
        if enter == 'end':
            break
        if enter in price:
            pay += price[enter]
        else:
            print('Такого товара нет в списке!')
    return pay


# Словарь с ценами на товары
price = {'мясо': 3, 'хлеб': 1, 'картошка': 0.5, 'вода': 0.2}
print(buy())  # Вызывает функцию покупки и выводит итоговую сумму

# Вложенные словари и доступ к элементам
users = {
    "Alex7": {"password": 9856214, "id": 1957},
    "Jimmy99": {"password": 1236487, "id": 9654},
    "Bob33": {"password": 9546752, "id": 6453},
}
print(users["Alex7"]["password"])  # Выводит пароль пользователя Alex7

# Создание словаря с использованием списка пар ключ-значение
d2 = dict([[1, 2], [3, 4], [5, 6]])
print(d2)  # Выводит {1: 2, 3: 4, 5: 6}

# Копирование словаря
d5 = d1.copy()
print(d1.items())  # Выводит пары ключ-значение словаря d1

# Обновление словаря d1 значениями из d2
d1.update(d2)
print(d1)  # Выводит объединенный словарь с элементами из d1 и d2

# Безопасное получение значения по ключу с помощью метода get()
default_value = "Неизвестно"
y = d1.get("c", default_value)
print(y)  # Выводит "Неизвестно", если ключ "c" отсутствует в d1
