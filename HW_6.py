# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# first_number = int(input("First number: "))
# step = int(input("Step element: "))
# quantity_number = int(input("Quantity of elements: "))

# def Arifmetic_progression(first_number, step, quantity_number):
#     array = [first_number]

#     for i in range(1, quantity_number):
#         next_element = array[i-1] + step
#         array.append(next_element)
    
#     return array

# print(Arifmetic_progression(first_number, step, quantity_number))


# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

size = int(input("Size array: "))

def create_array(size):

    list_test = [0] * size

    for i in range(size):
        number = int(input("input element: "))
        list_test[i] = number
    print(list_test)
        
    return list_test

array = create_array(size)

minArray = int(input("Input array min quantity: "))
maxArray = int(input("Input array max: quantity: "))

list_index = list()
for i in range(len(array)):
    if minArray <= array[i] <= maxArray:
        print(i)