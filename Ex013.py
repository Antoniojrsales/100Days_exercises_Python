#Crie um programa que leia o salario de um funcionario e mostre seu novo salario com um aumento de 15%

def aumento_salario(valor, porcentagem):
    return valor + (valor * porcentagem / 100)

while True:
    print('='*7,'Aumento Salarial','='*7)  
    salario = input('Qual é o salário do funcionário? R$')
    valor_aumento = input('Qual a porcentagem de aumento: ')

    try:
        print('='*14,'Resultado','='*14) 
        salario_float = float(salario)
        valor_aumento_int = int(valor_aumento)
        aumento = aumento_salario(salario_float, valor_aumento_int)
        print(f'Um funcionário que ganhava R${salario_float:.2f} com {valor_aumento_int}% de aumento passa a receber R${aumento:.2f}')
        break

    except ValueError:
        print('Erro: Por favor, digite um valor válido.')