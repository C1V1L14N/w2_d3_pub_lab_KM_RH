# from pub import Pub

class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunk_level = 0

                    ##### Buying a drink #####
        # Take money off customer
        # Add to pissed level

    def take_money_off_customer(self, monies):   
        self.wallet -= monies
        
    def increase_fun(self, units):    
        self.drunk_level += units

    def buy_drink(self, drink):
        self.take_money_off_customer(drink["price"])
        self.increase_fun(drink["units"])

    