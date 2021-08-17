valor = int(input('Até quanto irá contar? '))
denominator = 1
s = 0
while denominator <= valor:
    num = 1 / denominator
    s += num
    denominator += 1
print(f'A soma da serie é {s}.')