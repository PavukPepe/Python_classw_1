while (True):
    print("Введите чило")
    num = input()
    if num.isdigit():
        num = int(num)
        cl = 0
        for i in range(1, num+1):
            if num % i == 0:
                cl += 1
        if cl == 1 or cl == 2:
            print("Число простое")
        else:
            print("Число нетпростое")
    else:
        print("Введенное значение не чиcло")
