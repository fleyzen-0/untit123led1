try:
    print("Розмір сторони квадрата: ")
    number = int(input())
    for i in range(number):
        for j in range(number):
            if i == 0 or i == number-1:
                print("*", end=" ")
            else:
                if j == 0 or j == number-1:
                    print(f"*", end= " ")
                else:
                    print(f" ", end=" ")
        print()
except Exception as ex:
    print("Erorr: ", ex)
finally:
    print(" Завдання виконано.")