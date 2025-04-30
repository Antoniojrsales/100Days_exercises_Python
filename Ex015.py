#Crie um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preco a pagar sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

def pagar_dias(dia):
    return dia * 60

def pagar_km(km):
    return km * 15 / 100

def main():
    while True:
        print('='*7,'Aluguel de veiculo','='*7)  
        dias = input('Quantos dias alugados: ')
        km = input('Quantos kms rodados: ')

        if km.isdigit() and dias.isdigit():
            print('='*12,'Resultado','='*12) 
            km_int = int(km)
            dias_int = int(dias)
            valor_km = pagar_km(km_int)
            valor_dias = pagar_dias(dias_int)
            print(f'O total a ser pago e de R${valor_km + valor_dias:.2f}')
            break

        else:
            print('Erro: Por favor, digite um valor válido.')

if __name__ == "__main__":
    main()