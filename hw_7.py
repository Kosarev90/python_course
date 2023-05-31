# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

def print_operationn_table(operation, num_rows = 6, num_colomns = 6):
    for row in range(1, num_rows + 1):
        for colomn in range(1, num_colomns + 1):
            result = operation(row, colomn)
            print(f"{result:<5}", end="")
        print()
    

print_operationn_table(lambda x, y: x*y)

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
#  насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
#  если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
#  Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
#  В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def rifmaCheck(rifma):
    lines = rifma.split(" ")
    countSyllables = None

    for line in lines:
        words = line.split("-")
        lineSyllables = [countLetter(word) for word in words]

        if countSyllables is None:
            countSyllables = lineSyllables
        elif countSyllables != lineSyllables:
            return "Пам парам"
    return "Парам пам-пам"


countLetter = lambda word: sum(word.count(vowel) for vowel in "аеёиоуыэюя")


rifma = input("Введите рифму Винни-Пуха: ")
result = rifmaCheck(rifma)
print(result)
