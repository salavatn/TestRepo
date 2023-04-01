
# Перечисление чисел через пробел:
number1 = map(int, input().split())
number2 = map(int, input().split())

# Сортировка чисел:
print(*sorted(number1, reverse=True))
print(*sorted(number2, reverse=True))
