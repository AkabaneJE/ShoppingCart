class Item:
    def __init__ (self,name,price):
        self.name = name
        self.price = price
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_item(self,item):
        self.items.append(item)
        self.total_cost += item.price
        print(f"{item.name} (${item.price})is added to cart. Total cost is now ${self.total_cost}")
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            self.total_cost -= item.price
            print(f"{item.name} (${item.price})is removed to cart. Total cost is now ${self.total_cost}")
    def empty_cart(self):
        self.items = []
        self.total_cost = 0
    def print_cart_info(self):
        print(f"The total cost is {self.total_cost}")
        for item in self.items:
            print(f"{item.name} ${item.price}")
cart = ShoppingCart()
toilet_paper = Item('Toilet Paper', 2)
apple = Item("apple", 1)


cart.empty_cart()
cart.print_cart_info()
cart.add_item(apple)
cart.add_item(toilet_paper)
cart.remove_item(apple)
cart.empty_cart()
cart.print_cart_info()


