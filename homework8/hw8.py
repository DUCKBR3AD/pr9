import random

def get_user_choice(ticket):
    user_choice = []
    for i, row in enumerate(ticket):
        print(f"Выберите число из строки {i+1}: {row}")
        while True:
            try:
                choice = int(input("Введите число: "))
                if choice in row:
                    user_choice.append(choice)
                    break
                else:
                    print("Некорректный выбор. Пожалуйста, выберите число из строки.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")
    return user_choice

def get_random_choice(ticket):
    random_choice = [random.choice(row) for row in ticket]
    return random_choice

def calculate_statistics(user_choice, random_choice):
    matches = sum(1 for user_num, random_num in zip(user_choice, random_choice) if user_num == random_num)
    return matches

def main():
    ticket = [ [ 1, 2, 3, 4, 5], [ 6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], ]
    
    user_choice = get_user_choice(ticket)
    random_choice = get_random_choice(ticket)
    
    print(f"Ваш выбор: {user_choice}")
    print(f"Случайный выбор: {random_choice}")
    
    matches = calculate_statistics(user_choice, random_choice)
    print(f"Количество совпадений: {matches}")

if __name__ == "__main__":
    main()
