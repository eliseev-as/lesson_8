n = int(input("Введите количество чисел: "))

number_list = list(map(int, input(f'Введите через пробел {n} чисел: ').split()))

number_list.insert(0, number_list.pop())

print(number_list)
