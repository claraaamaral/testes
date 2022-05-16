from listas import *
import unittest

class TestProduto (unittest.TestCase):
    def Teste_reposicao(self):
        situacao1 = [('sabonete', 2), ('condicionador', 5), ('shampoo', 10)]

        self.assertEqual(1, QuantidadeMenorCinco(situacao1))

    def test_entrada(self):

        self.assertEqual(saida(situacao1), 1)
