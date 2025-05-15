# Create a program what read a number interger any and show in screen the your tabuada

def tabuada():
    # Define separators visuals for organize output in the terminal
    separador_longo = '=' * 17
    separador_curto = '=' * 12

    while True:  # Loop infinito para garantir entrada válida
        print(separador_longo, 'Tabuada', separador_longo)  # Exibe um título estilizado
        valor = input('Digite um número para ver a sua tabuada: ')  # Solicita um número ao usuário
        print()

        if valor.isdigit():  # Verifica se a entrada é um número inteiro positivo
            valor_int = int(valor)  # Converte a entrada para um número inteiro
            print(separador_curto)  # Imprime o separador curto
            tabuada_lista = [f'{valor_int} x {i:2} = {i * valor_int}' for i in range(1, 11)]  # Cria a lista com os cálculos da tabuada
            
            print('Resultado')  # Exibe o cabeçalho da tabuada
            for item in tabuada_lista:  # Percorre a lista e imprime cada linha da tabuada
                print(item)
            
            print(separador_curto)  # Exibe o separador final
            break  # Sai do loop após exibir a tabuada
        else:
            print('Erro: Por favor, digite um número inteiro válido.')  # Exibe uma mensagem de erro caso a entrada seja inválida

if __name__ == "__main__":
    tabuada()  # Executa a função apenas se o script for rodado diretamente
