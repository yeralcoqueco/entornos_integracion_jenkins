import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    #Add

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
        
    #Substract

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(-2, self.calc.substract(2, -4))
        self.assertEqual(6, self.calc.substract(-2, 6))
        self.assertEqual(1, self.calc.substract(1, 0))
        
    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())
        
    #Divide

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)
        
    #Multiply
    
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
    
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "7", 9)
        self.assertRaises(TypeError, self.calc.multiply, 6, "3")
        self.assertRaises(TypeError, self.calc.multiply, "1", "8")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 1, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 6, object())
        
    @patch('app.util.validate_permissions', create=False)
    def test_multiply_with_user_withour_permissions(self, _validate_permissions):
       self.assertRaises(TypeError, self.calc.multiply, "7", 9)
        
    #Power
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(32, self.calc.power(2, 5))
        self.assertEqual(9, self.calc.power(3, 2))
        
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "7", 9)
        self.assertRaises(TypeError, self.calc.power, 6, "3")
        self.assertRaises(TypeError, self.calc.power, "1", "8")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 1, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 6, object())
        
    #Square root
    
    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(10, self.calc.square_root(100))
        self.assertEqual(5, self.calc.square_root(25))
        
    def test_square_root_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square_root, "7")
        self.assertRaises(TypeError, self.calc.square_root, None)
        self.assertRaises(TypeError, self.calc.square_root, object())
    
    def test_square_root_method_fails_with_number_is_lower_than_zero(self):
        self.assertRaises(TypeError, self.calc.square_root, -1)
        self.assertRaises(TypeError, self.calc.square_root, "-4")
        
    #Log10
    
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(1, self.calc.log10(10))
        
    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "7")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())
    
    def test_log10_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -0)
        self.assertRaises(TypeError, self.calc.log10, "0")

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
