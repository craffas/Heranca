#Inicio do Programa.
#Criando Classe Mãe:
class Pessoa:
    #Método Construtor
    def __init__(self, nome, cpf, rg, idade):
        #Atributos da Classe.
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade

    #Chamando Atributos "Método Get"
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_rg(self):
        return self.rg

    def get_idade(self):
        return self.idade

    #Método de Sobreescrever Classe
    def __str__(self):
        return f'\nNome: {self.nome}\nCPF: {self.cpf}\nRG: {self.rg}\nIdade: {self.idade}'


