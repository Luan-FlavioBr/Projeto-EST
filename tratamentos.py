def lerfloat(entry):
    try:
        numero = float(entry)
    except ValueError:
        return None
    else:
        return numero