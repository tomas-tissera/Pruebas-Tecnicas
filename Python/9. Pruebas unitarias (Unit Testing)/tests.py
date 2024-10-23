from main import op1
import unittest

class TestCalcularAreaCirculo(unittest.TestCase):

    def test_area_con_radio_positivo(self):
        self.assertAlmostEqual(op1(5), 78.53981633974483)

    def test_area_con_radio_cero(self):
        self.assertEqual(op1(0), 0)

    def test_area_con_radio_negativo(self):
        with self.assertRaises(ValueError) as context:
            op1(-1)
        self.assertEqual(str(context.exception), "El radio no puede ser negativo.")

    def test_area_con_radio_no_numerico(self):
        with self.assertRaises(ValueError) as context:
            op1("dos")
        self.assertEqual(str(context.exception), "El radio debe ser un número.")

    def test_area_con_radio_flotante(self):
        self.assertAlmostEqual(op1(2.5), 19.634954084936208)

if __name__ == '__main__':
    unittest.main()
