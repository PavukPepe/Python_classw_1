import random

print("Угадайте число от 0 до 10")

num = random.randint(0, 10)
user = int(input("Введите число: "))

while user != num:
    if user > num:
        print("Меньше...")
    else:
        print("Больше...")
    user = int(input("Введите число: "))

print("Поздравляю, вы угадали")