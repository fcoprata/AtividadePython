
lista = []

while (1):
    name = input("Digite o nome: ")    
    if name == "parar":
        break
    else:
        lista.append(name)

print(sorted(lista))
