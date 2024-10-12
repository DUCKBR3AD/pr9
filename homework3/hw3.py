list = []

while True:
    inp = input("Введите число или end чтобы остановить программу: ")
    if inp == "end":
        print(list)
        break
    else:
        try:
            last = int(inp) % 2
            if last != 0:
                list.append(int(inp))
        except ValueError:
            print("Некорректный ввод. Введите число.")
            break
    
