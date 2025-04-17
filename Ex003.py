#Create one program what read two numbers and show the sum between them

# Define uma função chamada 'somar_valores' que realiza a soma de dois números digitados pelo usuário
def somar_valores():
    # Solicita ao usuário que digite o primeiro e segundo valor e armazena como string
    valor_um = input('Digite o primeiro valor: ') 
    valor_dois = input('Digite o segundo valor: ') 

    # Verifica se os dois valores digitados são compostos apenas por dígitos (números inteiros positivos)
    if valor_um.isdigit() and valor_dois.isdigit():
        valor_um_int = int(valor_um) # Converte as strings para inteiros
        valor_dois_int = int(valor_dois) # Converte as strings para inteiros
        soma = valor_um_int + valor_dois_int # Calcula a soma dos dois valores
        print(f'A soma entre {valor_um_int} e {valor_dois_int} = {soma}') # Exibe o resultado formatado
    else:
        # Caso um ou ambos os valores não sejam válidos, exibe uma mensagem de erro
        print('Valor inválido. Digite um valor válido.')

somar_valores() # Chama a função para ser executada