#Create a program what read a number interger and show in screen the your successor and its prececessor

# Define the function what calculate the successor and its prececessor of a number
def sucessor_antecessor():
    # Loop infinite for repeat until the user to type a value valid
    while True:
        numero = input('Digite um numero: ')# Solicita ao usuário que digite um valor
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