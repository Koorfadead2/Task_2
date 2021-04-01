n = int(input("Введите количество строк: "))
matr = [[0 for x in range(n)] for t in range(n)]
k = 1
low_value = 0
high_value = n-1
count = int((n+1)/2)
for i in range(count):
    for j in range(low_value, high_value+1):
        matr[i][j] = k
        k += 1
    for j in range(low_value+1, high_value+1):
        matr[j][high_value] = k
        k += 1
    for j in range(high_value-1, low_value-1, -1):
        matr[high_value][j] = k
        k += 1
    for j in range(high_value-1, low_value, -1):
        matr[j][low_value] = k
        k += 1
    low_value += 1
    high_value -= 1

for i in range(n):
    for j in range(n):
        print(matr[i][j], end = "\t")
    print()