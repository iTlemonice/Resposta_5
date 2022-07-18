frase = input('Digite uma frase: ')
nova_frase = list(frase)

frase_format = nova_frase[::-1]

for letra in frase_format:
    print(f'{letra}', end='')