import unittest
from app import Product

class TestApp(unittest.TestCase):
    def setUp(self):
        self.new_product = Product("jacket","large","2000","20")

    def test_init(self):
        self.assertEqual(self.new_product.name,"jacket")
        self.assertEqual(self.new_product.description,"large")
        self.assertEqual(self.new_product.price,"2000")
        self.assertEqual(self.new_product.quantity,"20")

if __name__ == '__main__':
    unittest.main            