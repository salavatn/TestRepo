num1 = int(input())
num2 = int(input())
num3 = int(input())

list_numbers = [num1, num2, num3]

for element in list_numbers:
    if element > 0:
        print(str(element)[::-1])
    else:
        print("-", str(element)[1:][::-1], sep="")
