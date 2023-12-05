def obterEstado(placa):
    estado_tabela = {
        "AAA": "Paraná",
        "BFA": "São Paulo",
        # ... Adicionar todas as sequências e estados da tabela ...
        "SDT": "Sequências ainda não definidas"
    }

    estado = estado_tabela.get(placa[:3], "Estado não encontrado")
    return estado