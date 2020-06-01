import unittest
import unittesting_calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(unittesting_calc.add(10, 5), 15)
        self.assertEqual(unittesting_calc.add(-1, 1), 0)
        self.assertEqual(unittesting_calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(unittesting_calc.subtract(10, 5), 5)
        self.assertEqual(unittesting_calc.subtract(-1, 1), -2)
        self.assertEqual(unittesting_calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(unittesting_calc.multiply(10, 5), 50)
        self.assertEqual(unittesting_calc.multiply(-1, 1), -1)
        self.assertEqual(unittesting_calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(unittesting_calc.divide(10, 5), 2)
        self.assertEqual(unittesting_calc.divide(-1, 1), -1)
        self.assertEqual(unittesting_calc.divide(-1, -1), 1)
        self.assertEqual(unittesting_calc.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, unittesting_calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            unittesting_calc.divide(10, 0) # using the context manager when using exceptions





if __name__ == '__main__':
    unittest.main()