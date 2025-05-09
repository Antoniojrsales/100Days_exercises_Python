#Crie um programa que leia quatro alunos e sorteie a ordem de apresentacao de um trabalho e mostre a ordem sorteada

from random import shuffle

lista_alunos = [input(f'Digite o {i}º aluno: ') for i in range(1, 5)]

shuffle(lista_alunos)

for i, lista in enumerate(lista_alunos):
    print(f'O {i + 1}º aluno escolhido foi {lista.title()}')