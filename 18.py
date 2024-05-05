def is_valid_date(date):
    day, month, year = map(int, date.split('/'))

    if year <= 0:
        return False

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    else:
        return False

date = input("Digite a data: ")
if is_valid_date(date):
    print("Data válida.")
else:
    print("Data inválida.")