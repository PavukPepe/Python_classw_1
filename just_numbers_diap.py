while (True):
    print("Введите нижнее заначение диапазона (включительно)")
    num1 = input()
    print("Введите верхнее заначение диапазона (включительно)")
    num2 = input()
    l = []
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        for j in range(num1, num2+1):
            cl = 0
            for i in range(1, j+1):
                if j % i == 0:
                    cl += 1
            if cl == 1 or cl == 2:
                l.append(j)
    else:
        print("Введенное значение не чиcло")
    print(*l)