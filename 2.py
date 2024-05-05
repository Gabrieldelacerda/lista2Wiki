def verificar_posicao_negativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "neutro"

numero = float(input("Digite um número: "))
resultado = verificar_posicao_negativo(numero)
print(f'O valor {numero} é {resultado}.')