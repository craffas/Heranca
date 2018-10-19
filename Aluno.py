#Inicio do programa.
from Pessoa import Pessoa
#Criando Classe Aluno:
class Aluno(Pessoa):
    def __init__(self, nome, cpf, rg, idade, ra, curso, nota):
        #Atributos da Classe:
        super().__init__(nome, cpf, rg, idade)
        self.ra = ra
        self.curso = curso
        self.nota = nota
    #Método Construtor:
    def __str__(self):
        return f'{super().__str__()}\nRA: {self.ra}\nCurso: {self.curso}\nNota: {self.nota}'

