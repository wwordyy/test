
user = input("Выберите уровень! ")
print()


level =  [{
    "Легкий":{
        "Вопрос 1" : "Что такое переменная?",
        "Вопрос 2" : "Программирование это - ....?",
        "Вопрос 3" : "Создатель Python - ...?"
    },
    "Ответы на 1 вопрос":
    {
        "Вариант 1" : "Это фиксированное значение, которое не может изменяться в процессе выполнения программы.",
        "Вариант 2" : "Специальный тип данных, который всегда содержит только целые числа.",
        "Вариант 3" : "Это именованная область памяти, используемая для хранения данных, которые могут изменяться в процессе выполнения программы."
    },
    "Ответы на 2 вопрос":{
        "Вариант 1" : "Процесс написания текстов на языке, который понимает только компьютер.",
        "Вариант 2" : "Процесс создания и модификации компьютерных программ, который включает написание инструкций на языках программирования.",
        "Вариант 3" : "Исключительно работа с числами и математическими формулами.",
    },
    "Ответы на 3 вопрос":{
        "Вариант 1" : "Стив Джобс",
        "Вариант 2" : "Билл Гейтс",
        "Вариант 3" : "Гвидо ван Россум",
    }
    }]


if user == "Легкий":
    # ЛЕГКИЙ УРОВЕНЬ 1 ВОПРОС
    print(level[0]["Легкий"]["Вопрос 1"])

    temp = level[0]["Ответы на 1 вопрос"]

    for key, value in temp.items():
        print(f"{key} -- {value}")

    print()
    print("Введите цифру правильного ответа:")
    user = int(input())

    if user == 3:
        print("Вы выбрали правильный вариант! :)")
    else:
        print("Эх жаль, неправильно :(")
    
    for i in range(3):
        print(" ")
# --------------------------------------------------------

# ЛЕГКИЙ 2 ВОПРОС
    print()
    print(level[0]["Легкий"]["Вопрос 2"])

    temp = level[0]["Ответы на 2 вопрос"]

    for key, value in temp.items():
        print(f"{key} -- {value}")

    print()
    print("Выберите цифру правильного ответа:")
    user = int(input())

    if user == 2:
        print("Вы выбрали правильный вариант! :) ")
    else:
        print("Фиаско :( ")

    for i in range(3):
        print(" ")
    
    
#-----------------------------------------------------

# ЛЕГКИЙ 3 ВОПРОС
    print()
    print(level[0]["Легкий"]["Вопрос 3"])

    temp = level[0]["Ответы на 3 вопрос"]

    for key, value in temp.items():
        print(f"{key} -- {value}")

    print()
    print("Выберите цифру правильного ответа:")
    user = int(input())

    if user == 3:
        print("Вы выбрали правильный вариант! Шаришь в этой теме получается :) ")
    else:
        print("Не получилось, не фортануло :( ")

    for i in range(3):
        print(" ")
# -------------------------------------------------------