n = int(input("Введите число строк: "))

number_list = []

for i in range(n):
    number = int(input(f'Введите число {i + 1}: '))
    number_list.append(number)

print(number_list[::-1])
