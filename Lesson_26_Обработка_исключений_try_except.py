# Обработка исключений, try, except, finally

# Создание строки
text = "Привет, мир!"
print(type(text))  # Выводит <class 'str'>, подтверждая, что переменная text является строкой

# Доступ к символам строки
print(text[0])  # Выводит 'П', первый символ строки
print(text[-1])  # Выводит '!', последний символ строки

# Срезы строк
print(text[1:5])  # Выводит 'риве', срез строки с 2-го по 5-й символы
print(text[:7])  # Выводит 'Привет,', срез с начала строки до 7-го символа
print(text[7:])  # Выводит 'мир!', срез с 8-го символа до конца строки

# Длина строки
print(len(text))  # Выводит 12, длина строки "Привет, мир!"

# Методы строк
print(text.upper())  # Выводит 'ПРИВЕТ, МИР!', все символы строки в верхнем регистре
print(text.lower())  # Выводит 'привет, мир!', все символы строки в нижнем регистре
print(text.replace("мир", "Вселенная"))  # Выводит 'Привет, Вселенная!', замена подстроки в строке

# Пример использования конструкций try, except и finally
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Ошибка: деление на ноль")  # Обработка исключения деления на ноль
finally:
    print("Конец программы")  # Блок finally выполнится в любом случае

# Обработка исключений при вводе данных от пользователя
while True:
    try:
        enter = float(input('Введите число: '))
        print(100 / enter)
        break
    except ValueError:
        print('Вы ввели не число! Попробуйте снова.')  # Обработка исключения неверного ввода
    except ZeroDivisionError:
        print('Делить на ноль нельзя! Попробуйте снова.')  # Обработка попытки деления на ноль
    finally:
        print('Попытка ввода завершена.')  # Информирование о завершении попытки

# Пример использования блока else
try:
    enter = float(input("Введите число: "))
    result = 100 / enter
except ValueError:
    print("Вы ввели не число!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
else:
    print(f"Результат деления: {result}")  # Выводится, если исключений не возникло
finally:
    print('Вывод финали')  # Выполняется в любом случае, независимо от наличия исключений

# Обработка исключений при работе с файлами
url_list = ["text.txt", "text2.txt", "text25.txt", "text3.txt"]
list_defect = []
list_info = []

for url in url_list:
    try:
        with open(url) as f:
            content = f.read()
            list_info.append(content)
    except FileNotFoundError:
        print(f"Файл {url} не найден.")
        list_defect.append(url)

print(f"Содержимое прочитанных файлов: {list_info}")
print(f"Список ненайденных файлов: {list_defect}")


import sys

# Предполагаем, что url_list должен быть списком строк, а не одной строкой
url_list = ["text.txt", "text2.txt", "text25.txt", "text3.txt"]

list_defect = []
list_info = []

# Обработка файлов и сбор информации
for url in url_list:
    try:
        # Использование менеджера контекста для безопасной работы с файлами
        with open(url) as r:
            list_info.append(r.read())
            print('Файл успешно прочитан:', url)
    except Exception as e:
        # Добавление url в список дефектных и вывод информации об ошибке
        list_defect.append(url)
        print('Ошибка при чтении файла:', url, e)

# Запись собранной информации и ошибок в файл save.txt
try:
    with open("save.txt", "a") as r:
        # Запись успешно прочитанного содержимого файлов
        for item in list_info:
            r.write(item + "\n")
        # Запись списка дефектных URL
        r.write("Список файлов с ошибками: " + str(list_defect) + "\n")
    print("Информация успешно сохранена в файле 'save.txt'.")
except Exception as e:
    print("Ошибка при записи в файл 'save.txt':", e)
'''
Этот код корректно обработает список URL-адресов, сохранит полученную информацию и список ошибок в файл save.txt, 
и выведет соответствующие сообщения. Использование with обеспечивает корректное закрытие файлов после их использования.
'''


# Обработка исключений при чтении файлов и записи информации в файл "save.txt"

# Предполагаемый список файлов для чтения
url_list = ["text.txt", "text2.txt", "text25.txt", "text3.txt"]

# Списки для хранения информации о прочитанных файлах и ошибках
list_defect = []
list_info = []

# Перебор всех URL в списке
for url in url_list:
    try:
        # Открытие и чтение содержимого каждого файла
        with open(url, 'r') as file:
            list_info.append(file.read())
    except FileNotFoundError:
        # Добавление информации о ненайденных файлах
        list_defect.append(url)
    except Exception as e:
        # Добавление информации о других ошибках чтения файла
        list_defect.append((url, str(e)))

# Запись собранной информации в файл "save.txt"
with open("save.txt", "w") as file:
    if list_info:
        # Запись информации из успешно прочитанных файлов
        file.write("\n".join(list_info))
    if list_defect:
        # Запись информации о файлах, которые не удалось прочитать
        file.write("Не удалось прочитать файлы:\n")
        file.write("\n".join(list_defect))

# Вывод сообщения о завершении работы программы
print("Программа завершила обработку файлов.")

'''
В этом коде программа не прекращает работу при возникновении ошибки чтения файла. 
Вместо этого ошибка записывается в список list_defect, и программа продолжает обработку следующих файлов. 
В конце работы информация о всех прочитанных файлах и ошибках записывается в файл save.txt.
'''
