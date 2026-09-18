"""Criando a CLASSE Pessoa"""
class Pessoa:
    def __init__(self, n, i, p, a): #dentro dos parenteses ficam os parâmetros que são os valores que o usuário vai me fornecer
        self.nome = n #self.nome é o atributo que vai armazenar o parâmetro que o usuário forneceu
        self.idade = i
        self.peso = p
        self.altura = a

    def apresentacao(self):
        print(f"O nome da pessoa consultada é {self.nome}; \nA idade dele(a) é:  {self.idade};")

        def fazer_anirversario(self):
            self.idade +=1 #Esse métodopega a idade do objeto e soma + 1
            print(f"Feliz aniversário, {self.nome}!!! Sua nova idade agora e´: {self.idade}.")

"""Criando os OBJETOS da classe pessoa"""
pessoa1 = Pessoa("Grace", 30, 55, 1.60)
pessoa2 = Pessoa("Alan", 25, 70, 1.80)

"""Chamando o método aprasentação"""
#pessoa1.apresentacao()
pessoa2.apresentacao()