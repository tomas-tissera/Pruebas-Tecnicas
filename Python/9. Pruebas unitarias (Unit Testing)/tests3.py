from main import op2
import unittest
class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calculadora.suma(2, 3), 5)
        self.assertEqual(self.calculadora.suma(-1, 1), 0)
        self.assertEqual(self.calculadora.suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(self.calculadora.resta(5, 3), 2)
        self.assertEqual(self.calculadora.resta(0, 0), 0)
        self.assertEqual(self.calculadora.resta(-1, 1), -2)

    def test_multiplicacion(self):
        self.assertEqual(self.calculadora.multiplicacion(2, 3), 6)
        self.assertEqual(self.calculadora.multiplicacion(-1, 1), -1)
        self.assertEqual(self.calculadora.multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(self.calculadora.division(6, 3), 2)
        self.assertEqual(self.calculadora.division(-6, 3), -2)
        self.assertEqual(self.calculadora.division(5, 2), 2.5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError) as context:
            self.calculadora.division(1, 0)
        self.assertEqual(str(context.exception), "No se puede dividir entre cero.")

if __name__ == '__main__':
    unittest.main()
