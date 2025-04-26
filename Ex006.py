#Create a program that read a number interger and display its double, triple and square root

# Define a function call 'dobro_triplo_raiz'
def dobro_triplo_raiz():
    while True:  # Loop infinite what continue until what the user type a value valid
        try:
            # Try convert the entry of user for a number interger
            valor = int(input('Digite um número inteiro: '))
            
            # If the conversion work out, show the results
            print(f'\nAnalisando o valor {valor}:') 
            print(f'O dobro é {valor * 2}')         
            print(f'O triplo é {valor * 3}')        
            print(f'A raiz quadrada é {valor ** 0.5:.2f}')              
            break  # end the program

        except ValueError:
            # if it occurs a error of conversion (ex: letras, símbolos), show message of error
            print('Erro: favor digitar um número inteiro válido.\n')

# Call the function for execute the program
dobro_triplo_raiz()
