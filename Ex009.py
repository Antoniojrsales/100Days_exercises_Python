# Crie um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

def tabuada():
    separador_longo = '=' * 28
    separador_curto = '=' * 12

    while True:
        print(separador_longo, 'Tabuada', separador_longo)
        valor = input('Digite um número para ver a sua tabuada: ')
        print()

        if valor.isdigit():
            valor_int = int(valor)
            print(separador_curto)
            tabuada_lista = [f'{valor_int} x {i:2} = {i * valor_int}' for i in range(1, 11)]
            print('Resultado')
            for item in tabuada_lista:
                print(item)
            print(separador_curto)
            break
        else:
            print('Erro: Por favor, digite um número inteiro válido.')

tabuada()