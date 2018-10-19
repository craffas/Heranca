#Importando Arquivos com Classes.
from Pessoa import Pessoa
from Funcionario import Funcionario
from Aluno import Aluno

#Introduzindo método de cadastramento:
print('Olá, seja bem vindo! Vamos realizar seu cadastro!!')
entrada = input('\nPara cadastrar uma Pessoa digite [P], Funcionário digite [F], Aluno digite [A]: ')

if entrada.upper() == 'P':
    #Chamando atributos da Classe Pessoa:
    nome = input('Digite nome completo: ')
    cpf = input('Digite seu CPF: ')
    rg = input('Digite seu RG: ')
    idade = int(input("Digite a sua idade: "))
    p1 = Pessoa(f'{nome}', f'{cpf}', f'{rg}', f'{idade}')
    print(f'\nCadastro concluído com sucesso, segue abaixo os dados:\n {p1}')
elif entrada.upper() == 'F':
    #Chamando atributos da Classe Funcionário:
    nome = input('Digite nome completo: ')
    cpf = input('Digite seu CPF: ')
    rg = input('Digite seu RG: ')
    idade = int(input("Digite a sua idade: "))
    matricula = int(input("Digite sua matricula: "))
    salario = int(input("Digite o salário do funcionário: "))
    setor = input("Digite o setor no qual será lotado: ")
    f1 = Funcionario(f'{nome}', f'{cpf}', f'{rg}', f'{idade}',
                     f'{matricula}', f'{salario}', f'{setor}')
    print(f'\nCadastro concluído com sucesso, segue abaixo os dados!\n {f1}')
elif entrada.upper() == 'A':
    #Chamando atributos da Classe Aluno:
    nome = input('Digite nome completo: ')
    cpf = input('Digite seu CPF: ')
    rg = input('Digite seu RG: ')
    idade = int(input("Digite a sua idade: "))
    ra = input("Digite seu RA: ")
    curso = input("Digite o nome do Curso: ")
    nota = int(input('Digite a nota: '))
    a1 = Aluno(f'{nome}', f'{cpf}', f'{rg}', f'{idade}',
               f'{ra}', f'{curso}', f'{nota}')
    print(f'\nCadastro concluído com sucesso, segue abaixo os dados!\n {a1}')
else:
    print('Opção inválida, tente novamente!')
