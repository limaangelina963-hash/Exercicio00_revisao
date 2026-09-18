"""criando a classe Pessoa""" 
class Pessoa:
    def __init__(self, n, i, p, a): #dentro dos parenteses ficam os parâmetros que são os valores que o usuário vai me fornecer
        self.nome = n #self.nome é o atributo que vai armazenar o parâmetro que o usuário forneceu
        self.idade = i
        self.peso = p
        self.altura = a

"""Criando os OBJETOS da classe pessoa"""
pessoa1 = Pessoa("Grace", 30, 55, 1.60)
pessoa2 = Pessoa("Alan", 25, 70, 1.80)

"""IMPRIMINDO ATRIBUTOS dos meus objetos"""
print("O nome da 1º pessoa cadastrada é: ", pessoa1.nome)
print("O nome da 2º pessoa cadastrada é: ", pessoa2.nome)

"""IMPRIMINDO TODOS OS ATRIBUTOS dos meus objetos"""
#1º forma de imprimir - segundo Ismael
print(vars(pessoa1))

#2º forma de imprimir - segundo Edimilson, Valdemilson
print(pessoa2.__dict__)

#3º forme de imprimir - Ismael
for atributo, valor in vars(pessoa2).items():
    print(atributo, ":", valor)

# forma de IDENTIFICAR OS ATRIBUTOS (sem os valores) de um objeto - segundo Maria Luiza
print(dir(pessoa2))