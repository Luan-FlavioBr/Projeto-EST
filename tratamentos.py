def lerfloat(entry):
    try:
        numero = entry.replace(',','.')
        numero = float(numero)
    except ValueError:
        return None
    else:
        return numero
    

def lerint(entry):
    try:
        numero = int(entry)
    except ValueError:
        return None
    else:
        return numero