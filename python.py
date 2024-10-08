"""a = int(input("Ведите число a:"))
b = int(input("Ведите число b:"))


if a  == 0 and b == 9:
    print("a = 0 и b == 9")
elif (a > 10) or (b < 10):
    print("a > 10 и b < 10")
else:
    print("a != 0")
"""

# Тернарный оператор 
"""
a = int(input("Ведите число a:"))
b = int(input("Ведите число b:"))
result = "a == 10 и b == 9" if (a == 10) and (b==9) else "a != 10 и b != 9"


print(result)
"""



# Цикл while 
# Кажыдй повтор цикла --- интерация
"""
a = int(input("Ведите число a:"))

while a > 10:
    print(a)
    if a == 11:
        print("Конец цикла")
    a -= 1
"""

# Цикл for

"""
for i in range (1, 21):
    if i == 13:
        print("конец!")
        continue
    print(i)
    """

# Оператор выбора match - case 
# a = input("Ведите a:")
"""match a:
    case 1: print("a = 1")
    case 2: print("a = 2")
    case 40: print("a = 40")
    case _: print("a неизвестное число")
"""

"""
match a:
    case "+":
        print(4 + 8)
    case "-":
        print(4 - 8)
    case "/":
        print(4 / 8)
    case "*":
        print(4 * 8)
    case _:
        print("чезабреттов")
"""
