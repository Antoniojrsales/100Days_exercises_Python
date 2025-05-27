# Create a program what read a number interger any and show in screen the your tabuada

def tabuada():
    # Define separators visuals for organize output in the terminal
    separador_longo = '=' * 17
    separador_curto = '=' * 12

    # Loop infinite for ensure valid entry
    while True:  
        print(separador_longo, 'Tabuada', separador_longo)
        valor = input('Digite um número para ver a sua tabuada: ')  # Prompts the user for a value
        print()

        if valor.isdigit():  # Check if input is a positive integer
            valor_int = int(valor)  # Converts the input for a number interger
            print(separador_curto)
            # Creating a list comprehension with multiplication table calculations
            tabuada_lista = [f'{valor_int} x {i:2} = {i * valor_int}' for i in range(1, 11)]  
            
            print('Resultado')
            # Travel through the list and prints each line of multiplication table calculations
            for item in tabuada_lista:  
                print(item)
            
            print(separador_curto)
            break  # Exit the loop after displaying the multiplication table calculations
        else:
            # Show an error message if the input is invalid
            print('Erro: Por favor, digite um número inteiro válido.')  

# Call the function for execute the program
if __name__ == "__main__":
    tabuada()
