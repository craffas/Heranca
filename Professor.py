#Calsse funcionário
from Pessoa import Pessoa

class Professor(Pessoa):
    #Método Construtor da Classe filha
    def __init__(self, nome, cpf, idade, matricula, salario, curso):
        #Atributos
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.curso = curso

    #Sobreescrever metodo STR da Classe Pessoa
    def __str__(self):
        return f'\n{super().__str__()}\nMatricula: {self.matricula}\nSalário: {self.salario}\nCurso: {self.curso}'
