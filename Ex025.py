#Crie um programa que leia o nome completo de uma pessoal e descubra se ela tem SILVa no nome
nome_completo = str(input('Qual o seu nome completo? ')).strip().upper()
print(f'Seu nome tem Silva? {"SILVA" in nome_completo} ')