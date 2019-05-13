import numpy as np

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.items = []
        self.employee_discount = emp_discount

    def add_item(self, name, price, quantity=1):
        self.items.append({"name":name,
                          "price": price,
                          "quantity":quantity,
                          "sub_total": price*quantity})
        self.total += price*quantity
        return self.total

    def list_item_prices(self):
        prices = []
        for item in self.items:
            prices += ([item["price"]] * item["quantity"])
        return(prices)

    def mean_item_price(self):
        return np.mean(self.list_item_prices())

    def median_item_price(self):
        return np.median(self.list_item_prices())

    def apply_discount(self):
        if self.employee_discount:
            return self.total*(100-self.employee_discount)/100
        return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if len(self.items):
            self.total -= self.items[-1]["price"]
            self.items.pop()
        else:
            return "There are no items in your cart!"
