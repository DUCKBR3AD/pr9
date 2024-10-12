even_list = []
odd_list = []
while True:
    inp = input("Введите число или end для завершения программы: ")
    if inp == "end":
        print(' Чётные числа:',even_list,'\n', 'Нечётные числа:', odd_list)
        print(' Количество чётных чисел: ',len(even_list), '\n', 'Количество нечётных чисел: ', len(odd_list))
        break
    else:
        try:
            num = int(inp)
            last = num % 2
            if last == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        except ValueError:
            print("Введите корректное число.")
            break
