from conversaoPlaca import numeroParaLetra
from estados import obterEstado

def main():
    placa_mercosul = input("Digite a placa no padrão Mercosul (LLLNLNN): ").upper()

    # Validar se a placa possui o formato correto antes de continuar

    letra_convertida = numeroParaLetra(int(placa_mercosul[3]))
    estado_identificado = obterEstado(placa_mercosul[:3])

    print(f"Letra convertida: {letra_convertida}")
    print(f"Estado identificado: {estado_identificado}")

if __name__ == "__main__":
    main()