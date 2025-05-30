#Crie um programa que faco o computador pensar em um numero inteiro entre 0 a 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa deve mostrar na tela se o usuario venceu ou perdeu
import os
from random import randint
import time

while True:
    print('-=' * 30)
    print('Vou pensar em um numero entre 0 e 5. Tente adivinhar.')
    print('-=' * 30)
    computador = randint(0, 5)
    valor = input('Em que numero eu pensei entre 0 e 5: ')
    if valor.isdigit():
        valor_int = int(valor)
        if valor_int <= 5:
            print('PROCESSANDO...')
            time.sleep(2)
            if computador != valor_int:
                print(f'Ganhei! eu pensei no numero {computador} e nao no {valor_int}')
            else:
                print(f'Parabens, vc adivinho o numero que era {computador}')
                break
        else:
            print('Erro: Por favor, digite um valor entre 0 e 5.')
            print()
    else:
        print('Erro: Por favor, digite um valor válido.')
        print()
    