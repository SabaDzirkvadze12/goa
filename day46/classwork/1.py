number = int(input("shemoitane ricxvi:  "))
list1 =[]
for i in number(1, number + 1):
    if number % i == 0:
            list1.append(i)
print(f"{number}-ის ყველა გამყოფია: {list1}")
