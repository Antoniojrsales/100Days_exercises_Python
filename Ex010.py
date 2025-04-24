#Crie um programa que que leia quanto de dinheiro a pessoa tem na carteira e mostre quantos dolares ele pode comprar
#considerando U$$1 = R$3,27

dolar = 3.27
def conversao(valor):
    dolares = valor / dolar
    return dolares
    
while True:
    print('='*10,'Conversor de Moeda','='*10)    
    valor = input('Quanto de dinheiro vc tem na carteira: R$ ')
    try:
        valor_float = float(valor)
        print('='*14,'Resultado','='*14)    
        dolares = conversao(valor_float)
        print(f'Com R${valor_float} vc pode comprar U$${dolares:.2f}')
        break

    except ValueError:
        print('Erro: Por favor, digite um valor válido.')

print("\nPrograma finalizado.")