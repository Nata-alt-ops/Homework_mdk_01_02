import unittest
from Calculator import Calculator
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.calculator = Calculator()
  #Each test method starts with the keyword test_
  def test_add(self):
    self.assertEqual(self.calculator.add(4,7), 11)

  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)

  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)

  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,2), 5)

  def test_root(self):
    self.assertEqual(self.calculator.root(16), 4)

  def test_module(self):
    self.assertEqual(self.calculator.module(-1), 1)
    
  def test_exponentiation(self):
    self.assertEqual(self.calculator.exponentiation(3,2), 9)
    
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()