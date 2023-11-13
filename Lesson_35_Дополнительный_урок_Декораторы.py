"""
Декораторы в Python - это мощный инструмент, который позволяет 
изменять поведение функций или классов без необходимости изменять их исходный код. 
Это делает код более модульным, гибким и позволяет переиспользовать функциональность.

Декораторы похожи на обертки вокруг функций или классов. 
Они принимают одну функцию и возвращают другую функцию, 
которая обычно расширяет или изменяет поведение исходной функции.
"""


# пример:
def decorator_1(func):
    def wrapper():
        print("До выполнения функции")
        func()
        print("После выполнения функции")

    return wrapper


@decorator_1
def hello():
    print("Привет, мир!")


hello()
"""
В этом примере мы определяем декоратор decorator, который принимает функцию func. 
Внутри декоратора мы определяем новую функцию wrapper, 
которая добавляет поведение до и после выполнения исходной функции. 
Затем мы используем синтаксис декоратора @decorator перед определением функции hello, 
чтобы применить декоратор к функции hello.

При вызове функции hello() будет выведено:
До выполнения функции
Привет, мир!
После выполнения функции

Таким образом, декоратор decorator расширил функциональность функции hello, 
добавив поведение до и после ее выполнения.
"""


# Декораторы также можно применять к классам.
# пример:
def decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def some_method(self):
            print("Дополнительный функционал")
            self.wrapped.some_method()

    return Wrapper


@decorator
class MyClass:
    def some_method(self):
        print("Основной функционал")


my_obj = MyClass()
my_obj.some_method()
'''
В этом примере мы определяем декоратор decorator, который принимает класс cls. 
Внутри декоратора мы определяем новый класс Wrapper, который оборачивает исходный класс. 
Мы добавляем дополнительный функционал в метод some_method, сохраняя при 
этом основной функционал исходного класса. Затем мы используем синтаксис 
декоратора @decorator перед определением класса MyClass, чтобы применить декоратор к классу.

При вызове метода some_method() объекта my_obj будет выведено:
Дополнительный функционал
Основной функционал
'''