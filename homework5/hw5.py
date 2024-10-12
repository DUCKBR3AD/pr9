def print_greater_elements(lst):
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            print(lst[i])
while True:
    numbers = [int(x) for x in input("Введите список чисел через пробел: ").split()]
    print_greater_elements(numbers)
