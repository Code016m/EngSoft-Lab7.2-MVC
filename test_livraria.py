import unittest

from livraria import (
    pesquisar_livros,
    consultar_livro,
    consultar_disponibilidade,
    consultar_disponibilidade_loja,
    consultar_preco,
    consultar_horario,
    consultar_localizacao,
    recomendar_livros
)


class TestLivraria(unittest.TestCase):

    def test_pesquisar_livro(self):
        resultado = pesquisar_livros("Dom Casmurro")

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Dom Casmurro")

    def test_consultar_informacoes_livro(self):
        livro = consultar_livro("Dom Casmurro")

        self.assertEqual(livro["titulo"], "Dom Casmurro")
        self.assertEqual(livro["autor"], "Machado de Assis")
        self.assertEqual(livro["preco"], 30.0)

    def test_consultar_disponibilidade(self):
        resultado = consultar_disponibilidade("Dom Casmurro")

        self.assertTrue(resultado)

    def test_consultar_disponibilidade_loja(self):
        resultado = consultar_disponibilidade_loja(
            "Dom Casmurro",
            "Loja Centro"
        )

        self.assertTrue(resultado)

    def test_consultar_preco(self):
        resultado = consultar_preco("Dom Casmurro")

        self.assertEqual(resultado, 30.0)

    def test_consultar_horario(self):
        resultado = consultar_horario()

        self.assertIsNotNone(resultado)

    def test_consultar_localizacao(self):
        resultado = consultar_localizacao()

        self.assertIsNotNone(resultado)

    def test_recomendar_livros(self):
        resultado = recomendar_livros()

        self.assertGreater(len(resultado), 0)


if __name__ == "__main__":
    unittest.main()