#Usando tuplas
tupla = ("a", "b", "c")
print(tupla)
print(tupla[0])
print(tupla[2])
print(tupla[1:])
print(tupla*2)
print(len(tupla))

#Tuplas não podem ter elementos alterados

for elemento in tupla:
    print(elemento)
    
#Também pode-se criar tuplas usando valores separados por vírgulas sem parênteses
tupla2 = 100,200,300
print(tupla2)

#Desempacotamento de valores com tuplas
a, b = 10, 20
print(a)
print(b)
a, b = b, a
print(a)
print(b)

#Tuplas com um único elemento
t1 = (1)
print(t1)
t2 = (1,)
print(t2)
t3 = 1,
print(t3)

#Tuplas vazias
t4 = ()
print(t4)
print(len(t4))

print()

#Criando tuplas a partir de listas
L=[1,2,3]
T=tuple(L)
print(T)

#Concatenação de tuplas
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)