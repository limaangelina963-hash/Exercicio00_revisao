list = ["maça", "banana", "mamao"]

#print(len(list)) #mostra o tamanho da lista.

list.append('lanja') #insere um item ao final da lista.
#print("lista após o uso do append: ", list)

list.insert(0, 'caqui') #insere o item na posição desejada
#print("lista após o uso do insert: ", list)

list.insert(3, 'uva')
#print("lista após o uso do insert do item uva na posição 3: ", list)

#list.remove('caqui') #remove um item através de um valor determinado

list.pop(0) #remove o último item da lista caso o index não seja determinado

print(list)

print(list.pop(2)) #mostra o item removido


numeros = [1,2,3,4,5]
print(numeros)

#1ª forma de inserir um valor:
numeros.insert(1,0)
print(numeros)

#2º forma de inserir um valor através da substituição:
numeros[1] = 50
print(numeros)

usuario1 = ["João", "111.333.444-07", "14/02/1990"]
print(usuario1)
#["João", "111.333.444-07", "14/02/1990"]
usuario1[0] = "João Pereira"
#["João Pereira", "111.333.444-07", "14/02/1990"]
print(usuario1)
usuario1[0] = "Lucas Pereira"
print(usuario1)
usuario1[2] = "14/02/2000"
print(usuario1)

usuario1.append("26 anos")     
print(usuario1)

usuario1.clear() #Apaga a lista
print(usuario1)