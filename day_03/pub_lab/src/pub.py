
# from customer import Customer

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = [
            {"name" : "fosters", "price": 500, "units": 2},
            {"name" : "corona", "price": 550, "units": 2},
            {"name" : "old Mount", "price": 550, "units": 3},
            {"name" : "tennents", "price": 400, "units": 1}
            ]

    def add_drink_stock(self, name, price, units):
        # name = "name"
        # price = 100
        self.drinks.append({"name": name, "price": price, "units": units})

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink["name"] == drink_name:
                return drink

    def add_money(self, money):
        self.till += money

    def check_customer_age(self, customer):
        return customer.age >= 18


    # get_customer()
        # return customer
    # get_pub
        # return pub

    
        


    

    # drink
        #name
        # price
        # unit level
        
                #### Extension ####
    # Make sure the `Pub` checks the `age` before serving the `Customer`.

    #  - `Pub` should refuse service above a certain level of `drunkenness`!


                #### Advanced Extensions ####
    # Each time a `Customer` buys `Food`, their `drunkenness` 
    # should go down by the `rejuvenation_level`

    # - Pub can have a `stock` (maybe a Dictionary?) to keep track the 
    #  amount of `drinks` available (Hard! Might need to change the drinks List 
    # to a drinks Dictionary)

    # - Pub can have a `stock_value` method to check the total value of its
    #  `drinks`