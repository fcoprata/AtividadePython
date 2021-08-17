
def replaceArray () :
    array = [-1,-2,-3,4,-5,6,7,-8,9,10,11]
    newArray = []
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = 0
            newArray.append(array[i])
        else:
            newArray.append (array[i])
    return newArray
print(replaceArray())