from estados import obterEstado

def main():
    placa = input("Digite a placa no padrão Mercosul (LLLNLNN): ").upper()

    estadoIdentificado = obterEstado(placa)

    print(f"Estado identificado: {estadoIdentificado}")

if __name__ == "__main__":
    main()