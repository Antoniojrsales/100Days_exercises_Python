#Crie um programa que leia a largura e altura de uma parede em metros e calcule a sua area e a quantidade de tinta necessaria para pinta la sabendo que cada litro de tinta pinta uma area de 2m

def conversao_area(largura, altura):
    return largura * altura

def pintura(area):
    return area / 2

while True:
    print('='*7,'Conversor Pintura','='*7)    
    largura = input('Digite a largura da parede: ')    
    altura = input('Digite a altura da parede: ')

    try:
        print('='*14,'Resultado','='*14) 
        largura_float = float(largura)
        altura_float = float(altura)
        area = conversao_area(largura_float, altura_float)
        tinta = pintura(area)
        print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area:.2f}m².')
        print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
        break

    except ValueError:
        print('Erro: Por favor, digite um número válido.')

print("\nPrograma finalizado.")