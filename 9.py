num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
numeros = [num1, num2, num3]
numeros_ordenados = sorted(numeros, reverse=True)
print("Números em ordem decrescente:", numeros_ordenados)