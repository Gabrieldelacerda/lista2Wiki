def decompor_numero(numero):
        unidades = numero % 10
        dezenas = (numero // 10) % 10
        centenas = (numero // 100) % 10

        return unidades, dezenas, centenas

def imprimir_decomposicao(numero):
    centenas, dezenas, unidades = decompor_numero(numero)

    if centenas > 0:
        if dezenas > 0 or unidades > 0:
            print(f"{centenas} centenas, ", end="")
        else:
            print(f"{centenas} centenas.")
    if dezenas > 0:
        if unidades > 0:
            print(f"{dezenas} dezenas, ", end="")
        else:
            print(f"{dezenas} dezenas.")
    if unidades > 0:
        print(f"{unidades} unidades.")
    else:
        print()

numeros = [320, 160, 200, 400, 20, 19, 2, 50]

for numero in numeros:
    print(f"{numero} = ", end="")
    imprimir_decomposicao(numero)