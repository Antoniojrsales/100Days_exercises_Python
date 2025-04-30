#Crie um programa que lei uma temperatura em Celsius e transforme em Fahrenheit

def converter_fahrenheit(valor):
    return (valor * 9/5) + 32

while True:
    print('='*5,'Conversor de Temperatura','='*5)  
    celsius = input('Informe a temperatura em C:')
    try:
        print('='*16,'Resultado','='*16) 
        celsius_float = float(celsius)
        valor = converter_fahrenheit(celsius_float)
        print(f'A temperatura de {celsius}C corresponde a {valor}F')
        break
    except ValueError:
        print('Erro: Por favor, digite um valor válido.')