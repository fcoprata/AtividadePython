valor = int(input("Digite um número:"))
for num in range(2,valor+1):
    if all(num%i!=0 for i in range(2,num)):
       print(num)