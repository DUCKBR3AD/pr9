def swap(lst):
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
    return lst


numbers = [int(x) for x in input("Введите список чисел через пробел: ").split()]
numbers = swap(numbers)
print(numbers)
