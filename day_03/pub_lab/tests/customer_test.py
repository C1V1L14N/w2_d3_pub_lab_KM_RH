import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jake", 28, 10000)
        self.customer2 = Customer("Barbera", 47, 20000)
        self.customer3 = Customer("Brooklyn", 17, 600)
        self.pub = Pub("The Pink Truncheon", 100)

        # list_of_customers = [{self.customer = Customer("Jake", 28, 10000)},
        #                      {self.customer2 = Customer("Barbera", 47, 20000)},
        #                      {self.customer3 = Customer("Brooklyn", 17, 600)}

    def test_customer_has_name(self):
        self.customer4 = Customer("Cool customer", 7, 1000000)
        self.assertIsNotNone(self.customer.name, "Customer does not exist")
        self.assertIsNotNone(self.customer2.name, "Customer does not exist")
        self.assertIsNotNone(self.customer3.name, "Customer does not exist")
        # assertIsNotNone(test variable, "Message If test failed")
        
                ##### Buying a drink #####
        # Take money off customer
        # Add money to pubs till
        # Give them a drink
        # Add to pissed level

    def test_take_money_off_customer(self):
        drink = self.pub.find_drink_by_name("fosters")
        monies = drink["price"]
        self.customer.take_money_off_customer(monies)
        self.assertEqual(9500, self.customer.wallet)
                    # take_money_off_customer(self, customer, monies):  

    def test_increase_fun(self):
        drink = self.pub.find_drink_by_name("corona")
        units = drink["units"]
        self.customer.increase_fun(units)
        self.assertEqual(2, self.customer.drunk_level)
        # def increase_fun(self, units):   

    def test_buy_drink(self):
        drink = self.pub.find_drink_by_name("tennents")
        self.customer.buy_drink(drink)
        self.assertEqual(9600, self.customer.wallet)
        self.assertEqual(1, self.customer.drunk_level)
    # {"name" : "tennents", "price": 400, "units": 1}
    # def buy_drink(self, drinks):


    


                #### MVP ####
#  - A `Customer` should be able to buy a `Drink` from the `Pub`, 
# reducing the money in its `wallet` and increasing the money in the 
# `Pub`'s `till`

                #### Extensions ####
#   - Add `alcohol_level` to the Drink, and a `drunkenness` level to the 
#         `Customer`. Every time a `Customer` buys a drink, 
#          the `drunkenness` level should go up by the `alcohol_level`