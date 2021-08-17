
lista = [] 
def soma():
    for i in range(10):
        val = int(input('Digite um número: '))
        lista.append(val)
    acum = sum(lista)
    return acum
print(soma())