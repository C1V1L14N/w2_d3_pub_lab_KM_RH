from src.pub import Pub
from src.customer import Customer

class CustomerHolder:
    def __init__(self):
        self.customer = Customer("Jake", 28, 10000)
        self.customer2 = Customer("Barbera", 47, 20000)
        self.customer3 = Customer("Brooklyn", 17, 600)
    
    def get_customer(self):
        return self.customer

    def get_customer2(self):
        return self.customer2

    def get_customer3(self):
        return self.customer3
