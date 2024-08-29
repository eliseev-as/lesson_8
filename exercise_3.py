m = int(input("Введите максимальную массу, которую может выдержать одна лодка: "))
n = int(input("Введите количество рыбаков: "))

fishermen = []
boats = []

for i in range(n):
    fishermen.append(int(input(f'Введите вес путешественника {i + 1}: ')))

for j in range(len(fishermen)):
    if fishermen[j] + min(fishermen) <= m:
        boats += [[fishermen[j], min(fishermen)]]
        fishermen[j] += m
        fishermen[fishermen.index(min(fishermen))] += m
    else:
        if fishermen[j] > m:
            continue
        else:
            boats += [[fishermen[j]]]

print(len(boats))
