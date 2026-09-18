estudante = input("Digite o nome do aluno: ")
notas = []

for i in range(4):
    n = float(input(f"Digite a (i+i)º nota: "))
    notas.append(n)
    soma = soma+n
    print(soma)
    média = soma/4

    print("\n Boletim de" estudante)
    print("------------------------------------")
    for i in notas:
        print(i)

    print("------------------------------------")
    