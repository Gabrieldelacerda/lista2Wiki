preco_file_duplo_ate_5kg = 4.9
preco_file_duplo_acima_5kg = 5.8
preco_alcatra_ate_5kg = 5.9
preco_alcatra_acima_5kg = 6.8
preco_picanha_ate_5kg = 6.9
preco_picanha_acima_5kg = 7.8
desconto_cartao_tabajara = 0.05

tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ").lower()
kg_carne = float(input("Digite a quantidade (Em kg) de carne: "))
pagamento_cartao_tabajara = input("A compra foi feita no cartão Tabajara? (sim/não): ")

if tipo_carne == "file duplo":
    preco_kg = preco_file_duplo_ate_5kg if kg_carne <= 5 else preco_file_duplo_acima_5kg
elif tipo_carne == "alcatra":
    preco_kg = preco_alcatra_ate_5kg if kg_carne <= 5 else preco_alcatra_acima_5kg
elif tipo_carne == "picanha":
    preco_kg = preco_picanha_ate_5kg if kg_carne <= 5 else preco_picanha_acima_5kg

valor_total = kg_carne * preco_kg
desconto = valor_total * desconto_cartao_tabajara if pagamento_cartao_tabajara else 0
valor_a_pagar = valor_total - desconto

print("\nCupom Fiscal: ")
print(f"Tipo de carne: {tipo_carne.capitalize()}")
print(f"Quantidade de carne: {kg_carne:.2f} kg")
print(f"Preço total: R$ {valor_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if pagamento_cartao_tabajara else 'Dinheiro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")