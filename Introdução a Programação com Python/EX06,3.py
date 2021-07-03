#Criando uma lista sem valores repetidos a partir de outras listas
L1 = [1,3,5,7,9,11,13,15,17,19,21,23,25]
L2 = [1,2,4,6,8,10,12,14,16,18,20,22,24,25]
Valores = L1[:]
x = 0
while x < len(L2):
    if L2[x] not in L1:
        Valores.append(L2[x])
    x += 1
print(sorted(Valores))