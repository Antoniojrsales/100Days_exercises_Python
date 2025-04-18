#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele

# Define uma função chamada 'destrinchando_string' que recebe um argumento chamado 'frase'
def destrinchando_string(frase):
    # Verifica se a frase não está vazia
    if frase:
        # Exibe a string informada com uma quebra de linha
        print(f'\nAnalisando o valor: "{frase}"\n')
        
        # Exibe o tipo primitivo da variável (deve ser 'str' no caso de entrada via input)
        print(f'Tipo primitivo: {type(frase).__name__}')
        
        # Verifica se a string contém apenas espaços
        print(f'Só tem espaços? {frase.isspace()}')
        
        # Verifica se a string é composta apenas por números
        print(f'É um número? {frase.isnumeric()}')
        
        # Verifica se a string é composta apenas por letras
        print(f'É alfabético? {frase.isalpha()}')
        
        # Verifica se a string é composta apenas por letras e números (sem espaços ou símbolos)
        print(f'É alfanumérico? {frase.isalnum()}')
        
        # Verifica se a string está toda em letras maiúsculas
        print(f'Está em maiúsculas? {frase.isupper()}')
        
        # Verifica se a string está toda em letras minúsculas
        print(f'Está em minúsculas? {frase.islower()}')
        
        # Verifica se a string está capitalizada (primeira letra maiúscula e o restante minúsculo)
        print(f'Está capitalizado (inicial maiúscula)? {frase.istitle()}')
    
    # Caso a entrada esteja vazia (usuário apenas apertou Enter)
    else:
        print('Erro: favor digitar algo.')

# Solicita uma entrada do usuário e chama a função para analisar a string
destrinchando_string(input('Digite algo: '))
