# Crie um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

def tabuada():
    while True:
        print('='*14,'Tabuada','='*14)
        valor = input('Digite um numero para ver a sua tabuada: ')
        print()
        if valor.isdigit():
            valor_int = int(valor)
            print('='*12)
            for i in range(1, 11):
                print(f'{valor_int} x {i:2} = {i * valor_int}')
            print('='*12)
            break

        else:
            print('Erro: Por favor, digite um número válido.')

tabuada()