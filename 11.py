salario = float(input("Digite o salário do colaborador: "))
if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento
print(f"Salário antes do reajuste: R$ {novo_salario:.2f}")
print(f"Percentual de aumento: R$ {percentual_aumento}%")
print(f"Valor do aumento: R${valor_aumento:.2f}")
print(f"Novo salário após o aumento: R${novo_salario:.2f}")