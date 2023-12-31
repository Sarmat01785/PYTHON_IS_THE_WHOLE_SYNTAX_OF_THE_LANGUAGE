# Функции def, определение и вызов
"""
Функции в языке программирования Python - это удобный способ организовать и структурировать код. 
Они позволяют определить блок кода, который может быть вызван из других частей программы.

Чтобы создать функцию в Python, используется ключевое слово "def", за которым следует 
имя функции и круглые скобки, содержащие аргументы функции. Затем после двоеточия следует блок кода, 
который будет выполняться при вызове функции.
"""


# Вот пример функции, которая выводит приветствие на экран:
def hello():
    print("Привет!")


# Вызов функции
hello()



'''
Функции могут принимать аргументы, которые могут быть использованы внутри функции. 
Вот пример функции, которая принимает имя пользователя в качестве аргумента и выводит приветствие с этим именем:
'''
def say_hello(name):
    print("Привет, " + name + "!")

# Вызов функции
say_hello("Алексей")


'''
Также функции могут возвращать значения с помощью ключевого слова return. 
Вот пример функции, которая возвращает сумму двух чисел:
'''
def add_numbers(a, b):
    return a + b

# Вызов функции и вывод результата
result = add_numbers(3, 5)
print(result) # 8




# print("До функции")
#
#
# def show():
#     print("Функция")
#
#
# print("После функции")

# print("До функции")
#
#
# def show():
#     print("Функция")
#
#
# show()
#
# print("После функции")

# print("До функции")
#
#
# def show():
#     print("Функция")
#
#
# show()
#
# print("После функции")
# show()


# def show():
#     print("Функция")
#
#
# def show2():
#     x = 7
#     return x
#
#
# y = show2()
# print(y)
#
# show()


# def show():
#     print("Функция")
#
#
# def show2():
#     x = 7
#     return x
#
#
# y = show2()
# z = show2() + 9
# print(z)
#
# print(show())


# def show():
#     print("Функция")


# def show2():
#     x = 7 + z
#     return x


# z = 7

# y = show2()
# print(y)
# z = 9
# print(show2())
