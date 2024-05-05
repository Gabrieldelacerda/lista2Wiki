def caixa_eletronico(valor):
    if valor < 10 or valor > 600:
        print("Valor de saque inválido. O valor mínimo é 10 reais e o máximo é 600 reais.")
        return

    notas_disponiveis = [100, 50, 10, 5, 1]
    notas_fornecidas = [0, 0, 0, 0, 0]

    for i, nota in enumerate(notas_disponiveis):
        while valor >= nota:
            valor -= nota
            notas_fornecidas[i] += 1

    print("Notas fornecidas:")
    for i, nota in enumerate(notas_disponiveis):
        if notas_fornecidas[i] > 0:
            print(f"{notas_fornecidas} nota(s) de {nota} reais.")

saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))
caixa_eletronico(saque)