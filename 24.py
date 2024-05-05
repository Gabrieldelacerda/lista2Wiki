def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def verificar_positivo_ou_negativo(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Neutro, safado!"

def verificar_inteiro_ou_decimal(numero):
    if numero == round(numero):
        return "Inteiro"
    else:
        return "Decimal"

numero1 = float(input("Digite um número real: "))
numero2 = float(input("Digite outro número real: "))

operacao = input("Digite a operação desejada: +, -, *, /")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida.")
    exit()

print(f"O resultado da operação é {resultado}.")
print(f"O resultado é {verificar_par_ou_impar(resultado)}, {verificar_positivo_ou_negativo(resultado)} e {verificar_inteiro_ou_decimal(resultado)}.")