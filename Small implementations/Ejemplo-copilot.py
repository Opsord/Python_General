#make a function that sort a list using bubble sort
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

lista = [5,3,1,2,4]
print(bubble_sort(lista))  
    
