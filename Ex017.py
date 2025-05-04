#Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo calcule e mostre o comprimento da hipotenusa

def hipotenusa(valor_oposto, valor_adjacente):
    return (valor_oposto ** 2 + valor_adjacente ** 2) ** 0.5

def main():
    while True:
        print('='*7,'Hipotenusa','='*7)
        oposto = input('Comprimento do cateto oposto: ')
        adjacente = input('Comprimento do cateto adjacente: ')

        try:
            print('='*12,'Resultado','='*12) 
            oposto_float = float(oposto)
            adjacente_float = float(adjacente)
            resultado = hipotenusa(oposto_float, adjacente_float)
            print(f'A hipotenusa vai medir {resultado:.2f}')
            break

        except ValueError:
            print('Erro: Por favor, digite um valor válido.')

if __name__ == "__main__":
    main()