from Pessoa import Pessoa
from Funcionario import Funcionario
from Professor import Professor
from Aluno import Aluno

print("Olá, sejam bem vindos ao meu programa.\n")
#Objeto da classe Pessoa
p1 = Pessoa("Rafael", '023.433.921.70', 22)

#Objeto em versão texto
print(p1)

#Objeto Funcionario
f1 = Funcionario("Sergio", '024.254.31', 50,
                 '2424', 100000,
                'DONO DO CEUB')
print(f1)

#Objeto Professor
p1 = Professor("João", '024.254.32', 24,
                 '2424', 10,
                'Artes')
print(p1)

#Objeto Aluno
a1 = Aluno("Keven", '024.254.33', 16,
                 '21802024', 8.5,
                'Educação Física')
print(a1)
