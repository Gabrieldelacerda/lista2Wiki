def calcular_media(n1, n2):
    return (n1 + n2) / 2

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = calcular_media(n1, n2)

if media == 10:
    situacao = "Aprovado com Dinstinção"
elif media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"A situação do aluno é {situacao}")