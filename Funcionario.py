#Inicio do Programa
from Pessoa import Pessoa
#Criando Classe Funcionario:
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, rg, idade, matricula, salario, setor):
        #Atributos da Classe:
        super().__init__(nome, cpf, rg, idade)
        self.matricula = matricula
        self.salario = salario
        self.setor = setor
        #Método construtor
    def __str__(self):
        return f'{super().__str__()}\nMatricula: {self.matricula}\nSalário: {self.salario}\nSetor: {self.setor}'