turno = input("Em que turno você estuda? M para matutino, V para vespertino e N para noturno: ")
if turno.upper() == 'M':
    print('Bom dia!')
elif turno.upper() == 'V':
    print('Boa tarde!')
else:
    print('Boa noite!')