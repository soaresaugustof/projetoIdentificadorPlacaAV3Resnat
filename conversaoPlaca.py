def numeroParaLetra(numero):
    letras = "ABCDEFGHIJ"
    if 0 <= numero <= 9:
        return letras[numero]
    else:
        return None