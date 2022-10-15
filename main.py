try:
    print("Висота прямокутника: ")
    number1 = int(input())
    print("Довжина прямокутника: ")
    number2 = int(input())
    for i in range(number1):
        for j in range(number2):
            if i == 0 or i == number1-1:
                print("*", end=" ")
            else:
                if j == 0 or j == number2-1:
                    print(f"*", end= " ")
                else:
                    print(f" ", end=" ")
        print()
except Exception as ex:
    print("Erorr: ", ex)
finally:
    print(" Завдання виконано.")