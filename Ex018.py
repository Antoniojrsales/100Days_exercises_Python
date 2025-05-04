#Crie um programa que leia um angulo e mostre na tela o valor de seno, cosseno e tangente

from math import sin, cos, tan, radians

def main():
    while True:
        angulo = input('Digite o angulo que vc deseja: ')
        try:
            angulo_float = float(angulo)
            radianos = radians(angulo_float)
            print(f'O angulo de {angulo_float} tem o seno de {sin(radianos):.2f}')
            print(f'O angulo de {angulo_float} tem o cosseno de {cos(radianos):.2f}')
            print(f'O angulo de {angulo_float} tem o tangente de {tan(radianos):.2f}')
            break

        except ValueError:
            print('Erro: Por favor, digite um valor válido.')

if __name__ == "__main__":
    main()
