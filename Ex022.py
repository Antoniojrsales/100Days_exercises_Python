#Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome em letras maiusculas
# O nome em letras minusculas
# Quantas letras tem ao todo somente letras
#Qual o primeiro nome e quantas letras tem

from time import sleep

nome = input('Digite o seu nome completo: ').strip()
separa_nome = nome.split()
print('Analisando seu nome...')
sleep(2)
print(f'Seu nome em maiusculo e {nome.upper()}')
print(f'Seu nome em maiusculo e {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'O seu primeiro nome e {separa_nome[0]} e ele tem {len(separa_nome[0])} letras')