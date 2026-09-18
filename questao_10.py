numero = int(input("Montar a tabuada de: "))
comecar = int(input("Começar por: "))
terminar = int(input("Terminar em: "))

print(f"Vou montar a tabuada de {numero} começando em {comecar} e terminando em {terminar}:")
for i in range(comecar, terminar + 1):
    print(f"{numero} X {i} = {numero * i}")