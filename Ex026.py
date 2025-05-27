# Crie um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra A
# Em que posicao ela aparece pela primeira vez
# Em que posicao ela aparece pela ultima vez 

frase = input('Digite uma frase: ').strip().lower()

print(f'A letra A aparece {frase.count("a")} veses na frase')
print(f'A primeira letra A apareceu na posicao {frase.find("a") + 1}')
print(f'A ultima letra A apareceu na posicao {frase.rfind("a") + 1}')