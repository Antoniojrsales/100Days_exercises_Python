# Create a program what read two notes of a student, calculate and show your average

# Define the function what will calculate the average of the two notes
def media():
    try:
        # Solicita ao usuário a primeira nota e converte para float
        nota_um = float(input('Digite a primeira nota do aluno: '))
        
        # Solicita ao usuário a segunda nota e converte para float
        nota_dois = float(input('Digite a segunda nota do aluno: '))
        
        # Calcula a média das duas notas
        media = (nota_um + nota_dois) / 2
        
        # Exibe o resultado formatado com uma casa decimal
        print(f'A média entre {nota_um} e {nota_dois} é {media:.1f}')
    
    # Caso ocorra um erro na conversão (ex: entrada inválida), exibe uma mensagem de erro
    except ValueError:
        print('Erro: por favor, digite um número válido.')

# Chama a função para executar o programa
media()
