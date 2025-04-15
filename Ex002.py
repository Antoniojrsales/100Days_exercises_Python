#Do one program what read the name of one peaple and show one message of welcome

def mensagem(nome):
    return f'E um prazer em lhe conhecer, {nome.title()}!'

msg = mensagem(input('Digite o seu nome: '))
print(msg)
