def encontrar_maior_numero(num1, num2):
    return num1 if num1 > num2 else num2

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
maior_numero = encontrar_maior_numero(num1, num2)
print(maior_numero)
