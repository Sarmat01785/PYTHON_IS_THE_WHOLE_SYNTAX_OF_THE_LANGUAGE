# Списки, тип данных list    Список это изменяемый тип данных.
"""
Список в Python - это упорядоченная коллекция элементов, которая может содержать 
значения разных типов данных. Списки очень полезны, когда вам нужно работать 
с несколькими значениями одновременно. 
"""
# Вот пример объявления списка:
my_list = [1, 2, 3, 4, 5]


# Можно создать список с элементами разных типов данных, например:
my_list = [1, "hello", True, 3.14]



"""
Вы можете получить доступ к элементам списка, используя индексы. 
Индексы в Python начинаются с 0. 
"""
# пример:
my_list = ["apple", "banana", "cherry"]

print(my_list[0])  # Выводит "apple"
print(my_list[1])  # Выводит "banana"
print(my_list[2])  # Выводит "cherry"



# Также, вы можете изменять значения элементов списка:
my_list = [1, 2, 3, 4, 5]

my_list[0] = 10  # Изменяет значение первого элемента на 10

print(my_list)  # Выводит [10, 2, 3, 4, 5]




# m = []
# print(type(m))  # Тип данных списки, в др языках программирования это массивы.


#    0  1  2  3  4
# m = [1, 2, 1, 3, 5]
# print(len(m))   # длина списка.
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[4])


#   -5 -4 -3 -2 -1
# m = [1, 2, 1, 3, 5]
# print(m[-1])   # обратная нумерация списка.


# m = [1, 2, 1, 3, 5, "a", [1, 2], ["s", "f"]]   # вложенные списки
# print(len(m))
# print(m[-1])
# print(m[-1][0])


# m = [[5, 6], [1, 2, ], ["s", "f"]]
# print(len(m))
# print(len(m[0]))

# m = [[5, 6], [1, 2, ], ["s", "f"]]
# m[0] = 9
# print(m)
# m = m[0] + 2
# print(m)


# m = [[5, 6], [1, 2, ], ["s", "f"]]
# m[1], m[2] = m[2], m[1]
# print(m)


# m = [[5, 6], [1, 2, ], ["s", "f"]]
# m = m + [7]
# print(m)

# m = [[5, 6], [1, 2, ], ["s", "f"]]
# m = m * 2
# print(m)

# m = [[5, 6], [1, 2, ], ["s", "f"]]
# n = list("string")
# print(n)

# m = [[5, 6], [1, 2, ], ["s", "f"]]
# n = list(range(10))
# print(n)


# n = list(range(10))
# for i in n:
#     print(i)

n = list(range(10))
m = []
for i in n:
    if i == 8:
        continue
    m += [i]
else:
    print(m)
