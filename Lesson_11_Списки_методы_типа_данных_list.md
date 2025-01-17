### Методы работы со списками в Python

Списки в Python являются одним из наибоее гибких встроенных типов данных. Они позволяют хранить последовательность элементов, которые могут быть различных типов. Далее мы рассмотрим основные методы, предоставляемые списками для управления этими элементами.

#### Создание списка чисел и вывод его длины


```python
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Выводит 5, количество элементов в списке
```

    5
    

#### Создаем список фруктов и ищем индекс и количество определенного элемента


```python
fruits = ["apple", "banana", "orange"]
print(fruits.index("orange"))  # Выводит индекс элемента "orange" в списке fruits
print(fruits.count("apple"))  # Выводит количество элементов "apple" в списке fruits
```

    2
    1
    

#### Сортировка списка чисел


```python
numbers.sort()  # Сортирует список numbers по возрастанию
print(numbers)  # Выводит отсортированный список numbers
```

    [1, 2, 3, 4, 5]
    

#### Меняем порядок элементов в списке фруктов на обратный


```python
fruits.reverse()
print(fruits)  # Выводит список fruits с элементами в обратном порядке
```

    ['orange', 'banana', 'apple']
    

#### Удаляем элемент "banana" из списка фруктов


```python
fruits.remove("banana")
print(fruits)  # Выводит список fruits без элемента "banana"
```

    ['orange', 'apple']
    

### Удаление элементов в цикле

Осторожно удаляем элементы из списка во время итерации, чтобы избежать пропуска элементов или ошибок во время выполнения.



```python
# Создаем список чисел и копируем его для безопасного удаления элементов в цикле
numbers = list(range(1, 21))
even_numbers = []
odd_numbers = numbers.copy()  # Делаем копию, чтобы избежать изменения списка во время итерации

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        odd_numbers.remove(number)

print("Нечетные числа:", odd_numbers)
print("Четные числа:", even_numbers)
```

    Нечетные числа: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    Четные числа: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    

## Работа с срезами списка

Срезы позволяют нам получить подмножество элементов списка. Это мощный инструмент для работы с данными.


```python
# Использование срезов для получения определенных элементов списка
slice_example = list(range(1, 21))
every_fifth = slice_example[::5]  # Получаем каждый пятый элемент
print("Каждый пятый элемент:", every_fifth)

# Получение всех элементов списка после пятого
after_fifth = slice_example[5:]
print("Элементы списка после пятого:", after_fifth)
```

    Каждый пятый элемент: [1, 6, 11, 16]
    Элементы списка после пятого: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
