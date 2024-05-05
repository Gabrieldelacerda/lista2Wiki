preco_gasolina = 2.5
preco_alcool = 1.9

litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível: A para álcool, G para gasolina: ").upper()

if tipo_combustivel == "A":
    if litros_vendidos <= 20:
        valor_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel == "G":
    if litros_vendidos <= 20:
        valor_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.06))
print(f"Valor: {valor_pagar:.2f}")
