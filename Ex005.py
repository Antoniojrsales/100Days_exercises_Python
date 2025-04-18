#Crie um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

# Define a função que calcula o antecessor e o sucessor de um número
def sucessor_antecessor():
    # Loop infinito para repetir até o usuário digitar um valor válido
    while True:
        numero = input('Digite um numero: ')# Solicita ao usuário que digite um número
        # Verifica se a entrada e valida e converte o valor para um número inteiro
        if numero and numero.isdigit():
            numero_int = int(numero)
            # Exibe o valor informado e os cálculos
            print(f'Analisando o valor {numero_int}')
            print(f'Seu antecessor é {numero_int - 1}')
            print(f'Seu sucessor é {numero_int + 1}')
            break# Interrompe o loop se o número for válido
        # Caso a conversão para inteiro falhe, captura o erro
        else:
            print('Erro: favor digitar um número inteiro.')
            continue# Recomeça o loop pedindo um novo número

# Chama a função para executar o programa
sucessor_antecessor()