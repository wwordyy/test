from math import sqrt
while True:
    one = int(input("Введите число a: "))
    two = int(input("Введите число b: "))

    print("Выберите операцию, которую хотите выполнить: +, -, *, /, //, **, %, sqrt ")
    print("Для выхода из программы введите 0")
    operation = input()



    match operation:
        case "+":
            print(one + two)
        case "-":
            print(one - two)
        case "/":
            if two != 0:
                print(one / two)
            else:
                print("Введите другое число")
        case "*":
            print(one * two)
        case "//":
            print(one // two)
        case "%":
            print(one % two)
        case "sqrt":
                root = int(input("Введите число из которого надо извлечь корень: "))
                print(sqrt (root))
                
            
        case "0":
            print("Выход из программы")
            break
        case "Выход из программы":
            print("Выход из программы")
            break
        case _:
            print("Неизвестное значeние")






