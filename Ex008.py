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

# Inicia um loop infinito que continuará até que uma entrada válida seja fornecida.
while True:
    # Solicita ao usuário que digite uma distância em metros e armazena a entrada como uma string.
    distancia = input('Digite uma distancia em metros: ')
    # Utiliza um bloco try-except para lidar com possíveis erros de conversão de tipo.
    try:
        # Tenta converter a string de entrada para um número de ponto flutuante (permite decimais).
        distancia_metros = float(distancia)
        # Chama a função 'converter_medidas' com o valor em metros
        km, hm, dam, dm, cm, mm = converter_medidas(distancia_metros)
        
        print(f'\nAnalisando a distancia digitada {distancia_metros}mts:')
        print(f'Km: {km:.1f}')
        print(f'Hm: {hm:.1f}')
        print(f'Dam: {dam:.1f}')
        print(f'Dm: {dm:.1f}')
        print(f'Cm: {cm:.1f}')
        print(f'Mm: {mm:.1f}')
        # Se a conversão e a impressão ocorrerem sem erros, o loop é interrompido.
        break

    # Captura a exceção ValueError, que ocorre se a entrada do usuário não puder ser convertida para um número.
    except ValueError:
        print('Erro: Por favor, digite um número válido.')

print("Programa finalizado.")