# Crie um programa que leia o nome completo e diga qual o seu primeiro nome e ultimo nome
nome = input('Digite o seu nome completo: ').strip()
nome_separado = nome.split()

print('Muito prazer em lhe conhecer!')
print(f'Seu primeiro nome e {nome_separado[0]}')
print(f'Seu ultimo nome e {nome_separado[-1]}')