from main import op2
import unittest
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def incrementar_salario(self, porcentaje):
        if porcentaje < 0:
            raise ValueError("El porcentaje de incremento no puede ser negativo.")
        self.salario += self.salario * (porcentaje / 100)

    def obtener_salario(self):
        return self.salario
    
class TestEmpleado(unittest.TestCase):

    def setUp(self):
        self.empleado = Empleado("Juan Pérez", 1000)

    def test_incremento_salario_positivo(self):
        self.empleado.incrementar_salario(10)  # Incrementar un 10%
        self.assertEqual(self.empleado.obtener_salario(), 1100)

    def test_incremento_salario_cero(self):
        self.empleado.incrementar_salario(0)  # Sin incremento
        self.assertEqual(self.empleado.obtener_salario(), 1000)

    def test_incremento_salario_negativo(self):
        with self.assertRaises(ValueError) as context:
            self.empleado.incrementar_salario(-5)
        self.assertEqual(str(context.exception), "El porcentaje de incremento no puede ser negativo.")

    def test_incremento_salario_grande(self):
        self.empleado.incrementar_salario(100)  # Incrementar un 100%
        self.assertEqual(self.empleado.obtener_salario(), 2000)

if __name__ == '__main__':
    unittest.main()