
import unittest
from src.pub import Pub
from src.customer_holder import CustomerHolder

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.customer_holder = CustomerHolder
        self.pub = Pub("The Pink Truncheon", 100)

    def test_pub_has_name(self):
        self.assertEqual("The Pink Truncheon", self.pub.name)

    def test_pub_has_till(self):
        self.assertLess(0, self.pub.till)

    def test_add_drink_stock(self):
        name = "Pink Flamingo"
        price = 10000
        units = 3
        self.pub.add_drink_stock(name, price, units)
        self.assertEqual(5, len(self.pub.drinks))

    def test_find_drink_by_name(self):
        test_drink = {"name" : "fosters", "price": 500, "units": 2}
        self.assertEqual(test_drink, self.pub.find_drink_by_name("fosters"))

    def test_add_money(self):
        self.pub.add_money(500)
        self.assertEqual(600, self.pub.till)

    def test_check_customer_age(self):
        customer = self.customer_holder.get_customer3()
        # self.assertEqual(False, self.pub.check_customer_age(customer))
        self.assertEqual(False, self.pub.check_customer_age(customer))