name = ["Петя", "Петя",  "вася", "коля", "Эдик"]


"""list_1 = ["Петя", 1, True, 4.5, "Вася", ["коля", 1]]


print(list_1[-1])

# Добавление 
# Индекс начинается с 0
name.append("Катя")
print(name)

name.insert(2, "Максим")
print(name)

name.extend([12, 18]) # Добавление спииска в списку
print(name)


# Удаление 
name.remove("коля") 
print(name)

index = name.pop(1)
print(index)
print(name)

del name[-1] # Удаление по индексу 
print(name)

name.clear() # Очистка списка
print(name)



# Поиск элементов 
index = name.index("Катя")
print(index)


count_dublicate = name.count("Петя")
print(count_dublicate)

# Сортировка 
name.sort() # Сортировка в алфавитном порядке, при работе с числами от меньшего к большему 
print(name)

name.reverse() # Сортировка в обратном порядке
print(name)

new_list = sorted(name) # Создает новый список, старый список остается неизменным 
print ("Новый", new_list)
print(name)

print(len(name)) # длина списка 
"""
# Индексы и срезы
print(name[0])
print(name[-1])
print(name[-2])

print(name[1:3]) # С первого по 3 элемнт НЕ ВКЛЮЧИТЕЛЬНО
print(name[0:-1:2])# С шагом 

print(name[::-1]) # Обратный порядок 


print(name[::]) # Выводит весь список
print(name[::2]) # Выводит нечетные 
print(name[1::2]) # Четные


name[0] = "Петух"
print(name)

numbers = [
    [1,2,3],
    [4,5,6],
    [33, 24, 26],
]
print(numbers[0][1])

for i in numbers:
    for g in i:
        print(g)

# Генераторы списков
list_numnbers = [num for num in range(1,11)]
print(list_numnbers)

print(max(list_numnbers))
print(min(list_numnbers))

print(sum(list_numnbers))

print(name + list_numnbers)
print(name * 3)


# Достаем элементы из списка 
"""
numbers = [1,2,3]
a,b,c = numbers
print(a,b,c)
"""

numbers = [1, 2, [3, 4], 5, 6]
a, *nums, b = numbers

print(a, nums, b)
print(*numbers)

"""
a, _, b, c, _, _ = numbers # Пропуск элементов 
print(a, b, c)
"""
a, b, (c, d), _, _ =numbers
print(a, b, c, d)

