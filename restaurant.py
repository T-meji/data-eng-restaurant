class Table:

    def __init__(self,num_of_people):
        self.bill = []
        self.num_of_people = num_of_people

    def order(self, item, price, quantity=1):
        for item_order in self.bill:
            if item_order["item"] == item and item_order["price"] == price:
                item_order["quantity"] += quantity
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for item_order in self.bill:
            if item_order["item"] == item and item_order["price"] == price:
                item_order["quantity"] -= quantity
                if quantity == 0:
                    del self.bill[item_order]
                return True
            else:
                return False

    def get_subtotal(self):
        subtotal = 0
        for item_order in self.bill:
            subtotal += item_order["price"] * item_order["quantity"]
        return subtotal

    def get_total(self):
        pass
    def split_bill(self):
        pass

