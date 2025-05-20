#Crie um programa que leia o nome de uma cidade e se o inicio tiver santo
cidade = input('Em que cidade vc nasceu? ').strip()
cidade_separada = cidade.split()
print(cidade_separada[0].upper() == 'SANTO')