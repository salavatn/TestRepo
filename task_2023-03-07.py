import math

a = (10, 20)
b = (5, 4)
length = round(math.sqrt((a[0]-b[0])**2 + (a[1] - b[1]) ** 2), 2)
print(length)
