import collections
#você manipula as listas abaixo, alterando o tamanho e valores
l1 = [1, 2, 4]
l2 = [3, 2, 1]



def comparar():
    if(collections.Counter(l1)==collections.Counter(l2)):
        return True #para iguais
    else:
        return False #para diferentes
print(comparar())