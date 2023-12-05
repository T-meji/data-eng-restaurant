class Table:

    def __init__(self,num_of_people):
        self.bill = []
        self.num_of_people = num_of_people

    def order(self,item,price,quantity=1):
        for objects in self.bill:
            if objects["item"] == item and objects["price"] == price:
                objects["quantity"] += quantity
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self):
        def remove(self, item, price, quantity=1):
        for item_order in self.bill:
            if item and price in item_order:
                item_order["quantity"] -= quantity
                if quantity == 0:
                    del self.bill[item_order]
                return True
            else:
                return False

    def get_subtotal(self):
        pass
    def get_total(self):
        pass
    def split_bill(self):
        pass

