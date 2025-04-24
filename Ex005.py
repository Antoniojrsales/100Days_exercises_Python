#Create a program what read a number interger and show in screen the your successor and its prececessor

# Define the function what calculate the successor and its prececessor of a number
def sucessor_antecessor():
    # Loop infinite for repeat until the user to type a value valid
    while True:
        numero = input('Digite um numero: ')# Prompt user to enter value
        # Check if the input is valid and convert the value for an interger
        if numero and numero.isdigit():
            numero_int = int(numero)
            print(f'Analisando o valor {numero_int}')
            print(f'Seu antecessor é {numero_int - 1}')
            print(f'Seu sucessor é {numero_int + 1}')
            break # Interrupt the loop if the value is valid
        # Case contrary, display the error
        else:
            print('Erro: favor digitar um número inteiro.')
            continue # Retorn to the loop

# Call the function for execute the program
sucessor_antecessor()