lista = []

#Roda 5x para o usuário digitar os 5 números
for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    lista.append(n)

print("Os números inseridos da lista são: ")
#Exibe cada item da lista
for i in lista:
    print(i)