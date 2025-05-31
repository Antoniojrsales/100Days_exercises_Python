#Crie um programa que leia a velocidade de um veiculo se ele ultrapassar a velocidade de 80km/h mostrei uma messagem dizem que ele foi multado. A multa vai custar R$ 7,00 por km acima do limite

limite = 80
multa_km = 7

radar = input('Qual e a velocidade do carro? ')
try:
    radar_int = int(radar)
    if radar_int > limite:
        exceder_limite = radar_int - limite
        valor_multa = exceder_limite * multa_km
        print(f'Vc foi multado por exceder a velocidade que e de {limite}km/h')
        print(f'Vc deve pagar uma multa de R${valor_multa:.2f}!')
    print('Tenha um bom dia! Dirija com seguranca!')

except ValueError:
    print('Erro: Por favor, digite um valor válido.')