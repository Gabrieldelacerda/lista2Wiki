preco_morango_ate_5kg = 2.5
preco_morango_acima_5kg = 2.2
preco_maca_ate_5kg = 1.8
preco_maca_acima_5kg = 1.5

kg_morango = float(input("Digite a quantidade (em kg) de morangos: "))
kg_maca = float(input("Digite a quantidade (em kg) de maçã: "))

total_morango = preco_morango_ate_5kg if kg_morango <= 5 else preco_morango_acima_5kg
total_maca = preco_maca_ate_5kg if kg_maca <= 5 else preco_maca_acima_5kg

valor_total = (kg_morango * total_morango) + (kg_maca * total_maca)

if (kg_morango + kg_maca) > 8 or valor_total > 25:
    valor_total *= 0.9

print(f"Total a pagar: R${valor_total:.2f}")