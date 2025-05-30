# Create a program what read two numbers and show the sum between them

# Define a function called 'somar_valores' what performs the sum of two number typed for the user
def somar_valores(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

def main():
    # Requests to the user what totype the first and second value and stores as string
    valor_um = input('Digite o primeiro valor: ') 
    valor_dois = input('Digite o segundo valor: ') 

    # Check if the two value requests they are compounds only of digits(number int positive)
    if valor_um.isdigit() and valor_dois.isdigit():
        valor_um_int = int(valor_um) # Converting strings for integers
        valor_dois_int = int(valor_dois) 
        soma = somar_valores(valor_um_int, valor_dois_int) # Calculate the sum of the two values
        print(f'A soma entre {valor_um_int} e {valor_dois_int} = {soma}') # displays the result formatted
    else:
        # Case one or both the values not be valid, displays one mesage of error
        print('Valor inválido. Digite um valor válido.')

# call the function for to be executed
if __name__ == '__main__':
    main()