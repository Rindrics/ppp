from cart import ShoppingCart
from product import Product


class TestShoppingCart():
    def test_cart_initially_empty(self):
        cart = ShoppingCart()
        assert cart.products == {}

    def test_add_product(self):
        cart = ShoppingCart()
        product = Product('Shoes', 'S', 'Black')
        cart.add_product(product, quantity=2)
        assert cart.products == {'SHOES-S-BLACK': {'quantity': 2}}

    def test_add_two_different_products(self):
        cart = ShoppingCart()
        product_one = Product('iPhone', 'L', 'Red')
        product_two = Product('T-shirt', 'XL', 'White')

        cart.add_product(product_one, quantity=2)
        cart.add_product(product_two, quantity=5)
        
        assert cart.products == {
            'IPHONE-L-RED': {'quantity': 2},
            'T-SHIRT-XL-WHITE': {'quantity': 5}
        }

    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product)

        assert cart.products == {}

    def test_remove_too_many_products(self):
        cart = ShoppingCart()
        product = Product('Shoes', 'S', "Blue")
        cart.add_product(product, quantity=1)
        cart.remove_product(product, quantity=2)
        assert cart.products == {}
