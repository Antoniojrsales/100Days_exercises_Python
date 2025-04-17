#Do one program what read the name of one peaple and show one message of welcome

# Define one call function 'mensagem' what receive one parameter called 'nome'
def mensagem(nome):
    #Return one string format with the name capitalized using .title()
    return f'E um prazer em lhe conhecer, {nome.title()}!'

# Requests to the user what to type the name and call the function 'mensagem' with that name
# The result and stored in variable 'msg'
msg = mensagem(input('Digite o seu nome: '))
print(msg) 
