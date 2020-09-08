import unittest
from product import Product


class ProductTestCase(unittest.TestCase):
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual('SHOES',
                         small_black_shoes.transform_name_for_sku()
        )
        small_pink_tank_top = Product('tank top', 'S', 'pink')
        self.assertEqual('TANKTOP',
                         small_pink_tank_top.transform_name_for_sku()
        )

    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual('BLACK',
                         small_black_shoes.transform_color_for_sku()
        )

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual('SHOES-S-BLACK',
                         small_black_shoes.generate_sku()
        )
