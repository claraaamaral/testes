from retornaLista import *
import unittest
class TestProduto (unittest.TestCase):
    def test_porcentagemVenda(self):
        self.assertEqual(percentual(7, 11), 0.6363)
        self.assertEqual(percentual(3, 11), 0.2727)
        self.assertEqual(percentual(1, 11), 0.0909)

    def test_percentual_status (self):
        situacao1=[(1,1,4),(1,2,3),(1,3,1),(2,1,3)]
        self.assertEqual(percentual_status(situacao1), (0.0909, 0.2727, 0.0909,0.0909))







