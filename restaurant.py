class Table:
    def __init__(self,num):
        self.bill = []
        self.number = num

    def order(self,item,price,quantity=1):
        for objects in self.bill:
            if objects["item"] == item and objects["price"] == price:
                objects["quantity"] += quantity
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self):
        pass
    def get_subtotal(self):
        pass
    def get_total(self):
        pass
    def split_bill(self):
        pass
