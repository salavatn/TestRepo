number = map(int, input().split())
number = list(number)

first = 0
last = -1

while True:
    if number[first] == number[last]:
        first += 1
        last -= 1

    elif number[first] != number[last]:
        num_x = number[first]
        num_y = number[last]
        number.pop(first)
        number.insert(first, num_y)
        number.insert(last, num_x)
        number.pop(last)
        break

print(*number)

