# Create a program what read two notes of a student, calculate and show your average

# Define the function what will calculate the average of the two notes
def media():
    try:
        # Prompts user for first note and converts to float
        nota_um = float(input('Digite a primeira nota do aluno: '))
        
        # Prompts user for second note and converts to float
        nota_dois = float(input('Digite a segunda nota do aluno: '))
        
        # Calculate the average of notes
        media = (nota_um + nota_dois) / 2
        
        # Displays the result formatted with one decimal place
        print(f'A média entre {nota_um} e {nota_dois} é {media:.1f}')
    
    # Case occur a error in conversion (ex: entrada inválida), displays a mesage of error
    except ValueError:
        print('Erro: por favor, digite um número válido.')

# Call the function for execute the program
media()
