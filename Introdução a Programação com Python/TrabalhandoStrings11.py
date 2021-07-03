#Pesquisa de strings, limitando o início ou o fim
s="um tigre, dois tigres, três tigres"
print(s.find("tigres"))
print(s.rfind("tigres"))
print(s.find("tigres", 7)) #Início=7
print(s.find("tigres", 30)) #Início=30
print(s.find("tigres", 0, 10)) #Início=0 fim=10