# Create a program what read a value in meters and display it converted in centimeters and milimeters

# Define a function call 'converter_medidas' what receive a value in meters as an argument.
def converter_medidas(metros):    
    km = metros / 1000    
    hm = metros / 100    
    dam = metros / 10    
    dm = metros * 10    
    cm = metros * 100    
    mm = metros * 1000
    # Return all the values converted in a tupla.
    return km, hm, dam, dm, cm, mm

# starting the loop infinite.
while True:
    distancia = input('Digite uma distancia em metros: ')
    # Using a block try-except.
    try:
        # Try convert the entry for a number of floating point.
        distancia_metros = float(distancia)
        # Call the function 'converter_medidas'
        km, hm, dam, dm, cm, mm = converter_medidas(distancia_metros)
        
        print(f'\nAnalisando a distancia digitada {distancia_metros}mts:')
        print(f'Km: {km:.1f}')
        print(f'Hm: {hm:.1f}')
        print(f'Dam: {dam:.1f}')
        print(f'Dm: {dm:.1f}')
        print(f'Cm: {cm:.1f}')
        print(f'Mm: {mm:.1f}')
        # Ends the block if all you are correct.
        break

    # If not, capture the exception ValueError, what occurs if the entry of user not can be converted for a valid number.
    except ValueError:
        print('Erro: Por favor, digite um número válido.')

print("Programa finalizado.")