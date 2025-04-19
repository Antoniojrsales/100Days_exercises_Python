#Create a program that read a number interger and display its double, triple and square root

# Define a function call 'dobro_triplo_raiz'
def dobro_triplo_raiz():
    while True:  # Loop infinite what continue until what the user type a value valid
        try:
            # Tenta converter a entrada do usuário para um número inteiro
            valor = int(input('Digite um número inteiro: '))
            
            # Se a conversão der certo, mostra os resultados
            print(f'\nAnalisando o valor {valor}:')  # Exibe o valor digitado
            print(f'O dobro é {valor * 2}')         # Calcula e exibe o dobro
            print(f'O triplo é {valor * 3}')        # Calcula e exibe o triplo
            print(f'A raiz quadrada é {valor ** 0.5:.2f}')  # Calcula e exibe a raiz quadrada com 2 casas decimais
            
            break  # Sai do laço após uma entrada válida
        except ValueError:
            # Caso ocorra um erro de conversão (ex: letras, símbolos), mostra mensagem de erro
            print('Erro: favor digitar um número inteiro válido.\n')

# Chama a função para executar o programa
dobro_triplo_raiz()
