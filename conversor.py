TAXAS_PARA_BRL = {
    "BRL": 1.00,
    "USD": 5.00,
    "EUR": 6.00
}


def converter_moeda(valor, moeda_origem, moeda_destino):
    """
    Converte um valor entre BRL, USD e EUR.

    Args:
        valor (float): Valor que será convertido.
        moeda_origem (str): Código da moeda de origem.
        moeda_destino (str): Código da moeda de destino.

    Returns:
        float: Valor convertido, arredondado para duas casas decimais.

    Raises:
        ValueError: Caso o valor seja negativo ou alguma moeda seja inválida.
    """

    moeda_origem = moeda_origem.upper()
    moeda_destino = moeda_destino.upper()

    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    if moeda_origem not in TAXAS_PARA_BRL:
        raise ValueError("Moeda de origem inválida.")

    if moeda_destino not in TAXAS_PARA_BRL:
        raise ValueError("Moeda de destino inválida.")

    valor_em_brl = valor * TAXAS_PARA_BRL[moeda_origem]

    valor_convertido = valor_em_brl / TAXAS_PARA_BRL[moeda_destino]

    return round(valor_convertido, 2)


def main():
    print("=== Conversor de Moedas ===")
    print("Moedas disponíveis: BRL, USD e EUR")

    try:
        valor = float(input("Digite o valor que deseja converter: "))

        moeda_origem = input("Digite a moeda de origem: ")
        moeda_destino = input("Digite a moeda de destino: ")

        resultado = converter_moeda(
            valor,
            moeda_origem,
            moeda_destino
        )

        print(
            f"{valor:.2f} {moeda_origem.upper()} = "
            f"{resultado:.2f} {moeda_destino.upper()}"
        )

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()