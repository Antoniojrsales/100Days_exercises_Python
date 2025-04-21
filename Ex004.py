# Create a program what read something on the keyboard and show in screen the your type primitive and all information possible on she

# Define a function called 'destrinchando_string' what receive a argument call 'frase'
def destrinchando_string(frase):
    # Check if the phrase not this empty
    if frase:
        print(f'\nAnalisando o valor: "{frase}"\n') # Analysing the value
        print(f'Tipo primitivo: {type(frase).__name__}') # The type primitve
        print(f'Só tem espaços? {frase.isspace()}') # Only have space
        print(f'É um número? {frase.isnumeric()}') # And a number
        print(f'É alfabético? {frase.isalpha()}') # It's alphabetical
        print(f'É alfanumérico? {frase.isalnum()}') # It's alphanumeric
        print(f'Está em maiúsculas? {frase.isupper()}') # It's in capital letters
        print(f'Está em minúsculas? {frase.islower()}') # It's in lowercase letters
        print(f'Está capitalizado (inicial maiúscula)? {frase.istitle()}') # It's capitalized
    
    # Case the entry be empty (user pressed Enter)
    else:
        print('Erro: favor digitar algo.')

# Requests a entry of user and call the function for to analyze the string
destrinchando_string(input('Digite algo: '))
