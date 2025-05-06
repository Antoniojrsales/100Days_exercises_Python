#Crie um programa que leia quatro nome de alunos e sorteie um e mostre quem ira apagar o quadro. 

from random import choice

lista_alunos = []
for i in range(1, 5):
    aluno = input(f'Digite o {i}º aluno: ')
    lista_alunos.append(aluno)

aluno_sorteado = choice(lista_alunos)

print(f'O aluno escolhido foi {aluno_sorteado.title()}')

'''Simplificando
lista_alunos = [input(f'Digite o {i+1}º aluno: ') for i in range(4)]
print(f'O aluno escolhido foi {choice(lista_alunos).title()}')'''