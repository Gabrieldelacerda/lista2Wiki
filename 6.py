def encontrar_maior_numero(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))

maior = encontrar_maior_numero(num1, num2, num3)
print(f'O maior número é {maior}')