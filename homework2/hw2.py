import math

def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Введите корректное число.")

def squares(a, b):
    start = math.ceil(min(a, b))
    end = math.floor(max(a, b))

    if a == start:
        start += 1
    if b == end:
        end -= 1

    return [i**2 for i in range(start, end + 1)]

while True:
    a = float_input("Введите число верхней границы: ")
    b = float_input("Введите число нижней границы: ")

    square_list = squares(a, b)

    if square_list :
        print(f"Квадраты целых чисел между {a} и {b}: {square_list}")
        break
    else:
        print(f"между {a} и {b} нет целых чисел")
        break
