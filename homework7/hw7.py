def rotate_list(lst):
    last_element = lst.pop()
    lst.insert(0, last_element)
    return lst

numbers = [int(x) for x in input("Введите список чисел через пробел: ").split()]
numbers = rotate_list(numbers)
print(numbers)
