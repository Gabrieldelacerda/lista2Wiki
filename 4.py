def verificar_vogal_consoante(letra):
    vogais = 'AEIOUaeiou'
    if letra.upper() in vogais:
        return "vogal"
    elif letra.isalpha():
        return "consoante"
    else:
        return "inválido"

letra = input("Digite uma letra: ")
resultado = verificar_vogal_consoante(letra)
print(f"A letra {letra} é uma {resultado}!")