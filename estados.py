def obterEstado(placa):
    estado_tabela = {
        "BFA": "São Paulo",
        "GKI": "São Paulo",
        "QSN": "São Paulo",
        "QSZ": "São Paulo",
        "KMF": "Rio de Janeiro",
        "LVE": "Rio de Janeiro",
        "RIO": "Rio de Janeiro",
        "RIP": "Rio de Janeiro",
        "RKV": "Rio de Janeiro",
        "MOX": "Espírito Santo",
        "MTZ": "Espírito Santo",
        "OCV": "Espírito Santo",
        "ODT": "Espírito Santo",
        "OVE": "Espírito Santo",
        "OVF": "Espírito Santo",
        "OVH": "Espírito Santo",
        "OVL": "Espírito Santo",
        "OYD": "Espírito Santo",
        "OYK": "Espírito Santo",
        "PPA": "Espírito Santo",
        "PPZ": "Espírito Santo",
        "QRB": "Espírito Santo",
        "QRM": "Espírito Santo",
        "RBA": "Espírito Santo",
        "RBJ": "Espírito Santo",
        "RQM": "Espírito Santo",
        "RQV": "Espírito Santo",
        "SDT": "Sequências ainda não definidas"
    }

    estado = estado_tabela.get(placa[:3], "Estado não encontrado")
    return estado