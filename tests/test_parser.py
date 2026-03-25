import unittest
from parser.cte_parser import extrair_dados_cte

class TestCTEParser(unittest.TestCase):
    def test_extrair_dados(self):
        dados = extrair_dados_cte("examples/exemplo_cte.xml")
        self.assertIn("CTe", dados)
        self.assertIn("Emitente", dados)
        self.assertIn("Destinatário", dados)

if __name__ == "__main__":
    unittest.main()
