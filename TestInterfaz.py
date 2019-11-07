import unittest
from parameterized import parameterized
from  InterfazComponent import Interfaz

class TestInterfaz(unittest.TestCase):

    @parameterized.expand([
        ('a'),
        ('b')
    ])
    def test_correct_row(self,x):
        self.assertFalse(Interfaz().set_valor_x(x))
    
if __name__ == '__main__':
    unittest.main()