nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite o segunda nota: '))
media = (nota1 + nota2) / 2
if 9 <= media <= 10:
    conceito = 'A'
elif 7.5 <= media <= 9:
    conceito = 'B'
elif 6 <= media <= 7.5:
    conceito = 'C'
elif 4 <= media <= 6:
    conceito = 'D'
elif 0 <= media <= 4:
    conceito = 'E'


print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")