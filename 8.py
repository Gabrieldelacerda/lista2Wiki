preco_produto1 = float(input('Digite o preço do primeiro produto: '))
preco_produto2 = float(input('Digite o preço do segundo produto: '))
preco_produto3 = float(input('Digite o preço do terceiro produto: '))

if preco_produto1 <= preco_produto2 and preco_produto1 <= preco_produto3:
    produto_mais_barato = "primeiro produto"
elif preco_produto2 <= preco_produto1 and preco_produto2 <= preco_produto3:
    produto_mais_barato = "segundo produto"
else:
    produto_mais_barato = "terceiro produto"

print(f"Você deve comprar o {produto_mais_barato}.")