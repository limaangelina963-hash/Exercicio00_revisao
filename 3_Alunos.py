class Aluno:
    def __init__(self, m, n, n1, n2, n3, n4, n5):
        self.matricula = m
        self.nome = n
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.nota4 = n4
        self.nota5 = n5

"""Criando os OBJETOS da classe Aluno"""
aluno1 = Aluno("2023001", "Grace", 8.5, 9.0, 7.5, 8.0, 9.5)
aluno2 = Aluno("2023002", "Alan", 7.0, 6.5, 8.0, 7.5, 8.5)

"""IMPRIMINDO ATRIBUTOS dos meus objetos"""
print("O nome do 1º aluno é: ", aluno1.nome)
print("A matrícula do 1º aluno é: ", aluno1.matricula)
print("As notas do 1º aluno são: ", aluno1.nota1, aluno1.nota2, aluno1.nota3)

print("O nome do 2º aluno é: ", aluno2.nome)
print("A matrícula do 2º aluno é: ", aluno2.matricula)
print("As notas do 2º aluno são: ", aluno2.nota1, aluno2.nota2, aluno2.nota3)

print(aluno1.__dict__)
print(aluno2.__dict__)