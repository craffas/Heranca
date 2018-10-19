#Calsse funcionário
from Pessoa import Pessoa

class Aluno(Pessoa):
    #Método Construtor da Classe filha
    def __init__(self, nome, cpf, idade, ra, nota, curso):
        #Atributos
        super().__init__(nome, cpf, idade)
        self.ra = ra
        self.nota = nota
        self.curso = curso

    #Sobreescrever metodo STR da Classe Pessoa
    def __str__(self):
        return f'\n{super().__str__()}\nRA: {self.ra}\nNota: {self.nota}\nCurso: {self.curso}'
