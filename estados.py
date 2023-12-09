def obterEstado(placa):
    primeira_letra = placa[0]
    segunda_letra = placa[1]
    terceira_letra = placa[2]

    # Verifica se a sigla é do Paraná
    if ('A' <= primeira_letra <= 'B' and 'A' <= terceira_letra <= 'Z') or \
       (primeira_letra == 'R' and segunda_letra == 'H' and 'A' <= terceira_letra <= 'Z'):
        return 'Paraná'

    # Verifica se a sigla é do Rio Grande do Sul
    elif (primeira_letra in ('I', 'J') and 'A' <= segunda_letra <= 'D' and 'Q' <= terceira_letra <= 'O'):
        return 'Rio Grande do Sul'

    # Verifica se a sigla é de Santa Catarina
    elif ((primeira_letra in ('L', 'M') and 'M' <= segunda_letra <= 'W' and 'M' <= terceira_letra <= 'R') or
          (primeira_letra == 'O' and segunda_letra == 'K' and ('D' <= terceira_letra <= 'H')) or
          (primeira_letra == 'Q' and 'H' <= segunda_letra <= 'J' and 'A' <= terceira_letra <= 'Z')):
        return 'Santa Catarina'

    # Caso não se encaixe em nenhum dos estados especificados
    else:
        return None