#Borrador

myList = list(range(15))
n = 3
print([myList[i:i + n] for i in range(0, len(myList), n)])