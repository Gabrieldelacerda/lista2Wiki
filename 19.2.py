def decompor_numero(numero):
    unidades = numero % 10
    dezenas = (numero // 10) % 10
    centenas = (numero // 100) % 10

    return centenas, dezenas, unidades

def imprimir_decomposicao(numero):
    centenas, dezenas, unidades = decompor_numero(numero)

    if centenas > 0:
        if dezenas > 0 or unidades > 0:
            print(f'{centenas} centenas, ', end='')
        else:
            print(f'{centenas} centenas')

    if dezenas > 0:
        if unidades > 0:
            print(f'{dezenas} dezenas, ', end='')
        else:
            print(f'{dezenas} dezenas')

    if unidades > 0:
        print(f'e {unidades} unidades')
    else:
        print()

numeros = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for numero in numeros:
    print(f'{numero} = ', end='')
    imprimir_decomposicao(numero)
