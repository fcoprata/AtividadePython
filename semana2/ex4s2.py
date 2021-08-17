num = int(input("Quantos números? "))
lista = [] 
def soma():
    for i in range(num):
        val = int(input('Digite um número: '))
        lista.append(val)
    acum = sum(lista)
    media = acum / num
    return media
print(soma())