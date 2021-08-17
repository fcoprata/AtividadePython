numero = int(input('Digite um número qualquer: '))    
resultado = numero % 2 # Pega o resto do número    
# True será par e impar False

def par():
    if resultado == 0:
        return True
    else:
        return False  
    

print(par())