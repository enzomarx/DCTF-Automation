import unittest
from src.LoginDominioWeb import enviar_dctf

class TestAutomation(unittest.TestCase):
    def test_enviar_dctf(self):
        #  adicionar testes para a função enviar_dctf
        try:
            enviar_dctf('12345678000195', '01/2023')
        except Exception as e:
            self.fail(f"enviar_dctf raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
