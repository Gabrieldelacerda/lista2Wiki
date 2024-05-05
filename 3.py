def verificar_genero(letra):
    if letra.upper() == "F":
        return "Feminino"
    elif letra.upper() == "M":
        return "Masculino"
    else:
        return "Undefined"

letra = input("Digite M para masculino e F para feminino. ")
genero = verificar_genero(letra)
print(f"O gênero é {genero}.")
