class Table:



    def remove(self, item, price, quantity=1):
        for item_order in self.bill:
            if item and price in item_order:
                item_order["quantity"] -= quantity
                if quantity == 0:
                    del self.bill[item_order]
                return True
            else:
                return False
