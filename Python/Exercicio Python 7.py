#Essa função recebe numeros e soma todos eles#
def somar (*numeros):
    total = 0
    for x in numeros:
        total+=x
    return total
i = somar(1,2,3,4,5,6,7,8,9,10)
print(i)