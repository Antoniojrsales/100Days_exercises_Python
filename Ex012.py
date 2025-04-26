#Crie um programa que leia o preco de um produto e mostre seu novo preco com 5% de desconto

def desconto_produto(valor, desconto):
    return valor - valor * desconto / 100

while True:
    print('='*7,'Desconto em Produto','='*7)    
    produto = input('Qual o preco do produto? R$')
    valor_desconto = input('Qual o desconto do produto: ')

    try:
        print('='*14,'Resultado','='*14) 
        produto_float = float(produto)
        valor_desconto_float = float(valor_desconto)
        desconto = desconto_produto(produto_float, valor_desconto_float)
        print(f'O produto que custava R${produto_float:.2f}, na promocao com desconto de {valor_desconto_float}% ira custar R${desconto:.2f}')
        break

    except ValueError:
        print('Erro: Por favor, digite um valor válido.')

print("\nPrograma finalizado.")