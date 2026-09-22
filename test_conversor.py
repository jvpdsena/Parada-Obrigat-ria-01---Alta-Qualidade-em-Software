import unittest

from conversor import converter_moeda


class TestConversorMoedas(unittest.TestCase):

    def test_usd_para_brl(self):
        resultado = converter_moeda(10, "USD", "BRL")
        self.assertEqual(resultado, 50.00)

    def test_brl_para_usd(self):
        resultado = converter_moeda(50, "BRL", "USD")
        self.assertEqual(resultado, 10.00)

    def test_eur_para_brl(self):
        resultado = converter_moeda(10, "EUR", "BRL")
        self.assertEqual(resultado, 60.00)

    def test_usd_para_eur(self):
        resultado = converter_moeda(10, "USD", "EUR")
        self.assertEqual(resultado, 8.33)

    def test_mesma_moeda(self):
        resultado = converter_moeda(100, "BRL", "BRL")
        self.assertEqual(resultado, 100.00)

    def test_valor_zero(self):
        resultado = converter_moeda(0, "USD", "BRL")
        self.assertEqual(resultado, 0.00)

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            converter_moeda(-10, "USD", "BRL")

    def test_moeda_origem_invalida(self):
        with self.assertRaises(ValueError):
            converter_moeda(10, "ABC", "BRL")

    def test_moeda_destino_invalida(self):
        with self.assertRaises(ValueError):
            converter_moeda(10, "BRL", "ABC")

    def test_minusculas(self):
        resultado = converter_moeda(10, "usd", "brl")
        self.assertEqual(resultado, 50.00)


if __name__ == "__main__":
    unittest.main()