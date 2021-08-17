# Define a função:
def exercicio():

    # Lista com os números lidos:
    numeros = []

    # Lê o primeiro número, garantindo que não seja zero:
    numero = 0
    while numero == 0:
        numero = int(input("Entre com o 1º número: "))
        if numero == 0:
            print("O 1º número não pode ser zero.")
    numeros.append(numero)

    # Lê os outros nove números:
    for i in range(49):
        numero = int(input("Entre com o %dº número: " % (i+2)))
        numeros.append(numero)

    # Obtém o maior valor e exibe-o na tela:
    maior = max(numeros)
    print("O maior valor é", maior)

    # Obtém o menor valor e exibe-o na tela:
    menor = min(numeros)
    print("O menor valor é", menor)

# Chama a função definida:
exercicio()