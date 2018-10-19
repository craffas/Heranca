#Classe Pessoa

class Pessoa:
    #Método Construtor
    def __init__(self, nome, cpf, idade):
        #Atributos
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    #Método Get
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_idade(self):
        return self.idade

    #Sobreescrever o método STR
    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}'