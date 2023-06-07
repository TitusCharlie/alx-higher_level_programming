#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = abs(number) % 10
print(i)

if number < 0:
    i = -i
    print(f"Last digit of {number} is {i} and is less than 6")

elif i > 5:
    print(f"Last digit of {number} is {i} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {i} and is 0")
else:
    print(f"Last digit of {number} is {i} and is less than 6")


