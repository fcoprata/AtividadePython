def menor(x,y):
    if x > y:
        min = y
    else:
        min = x

    return min

def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))

    print("Menor: ", menor(x,y))
    print()
    
while True:
    menu()
