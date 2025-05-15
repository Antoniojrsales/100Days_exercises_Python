#Crie um programa que leia um valor e mostre na tela cada um dos digitos separados (unidade, dezena, centena, milhar)

separador_longo = '=' * 16
separador_curto = '=' * 12

while True:
    print(separador_curto, 'Analisando Numero', separador_curto)
    valor = input('Informe um numero: ')
    if valor.isdigit():
        print(separador_longo, 'Resultado', separador_longo)
        valor_int = int(valor)
        print(f'Analisando o numero {valor}')
        unidade = valor_int // 1 % 10
        dezena = valor_int // 10 % 10
        centena = valor_int // 100 % 10
        milhar = valor_int // 1000 % 10
        print(f'Unidade: {unidade}')
        print(f'Dezena: {dezena}')
        print(f'Centena: {centena}')
        print(f'Milhar: {milhar}')
        break
    else:
        print('Erro: Por favor, digite um valor válido.')