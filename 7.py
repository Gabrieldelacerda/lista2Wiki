def encontrar_maior_numero(num1, num2, num3):
    return max(num1, num2, num3)

def encontrar_menor_numero(num1, num2, num3):
    return min(num1, num3, num2)

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))

maior_num = encontrar_maior_numero(num1, num2, num3)
menor_num = encontrar_menor_numero(num1, num2, num3)
print(f'O maior numero É {maior_num}')
print(f'O menor número é {menor_num}')