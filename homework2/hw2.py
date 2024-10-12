a = int(input("a: "))
b = int(input("b: "))

list = []

for i in range(a+1,b):
    i = i ** 2
    list.append(i)
  
print(list)
