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
        return round(float(subtotal), 2)

    def get_total(self, gratuity=0.1):
        # Calculate Sub Total
        subtotal = self.get_subtotal()

        # Calculate Service Charge
        service_charge = subtotal * gratuity

        # Calculate Total
        total = subtotal + gratuity

        # Format the results as strings in British pounds and pence
        formatted_subtotal = "£{:.2f}".format(subtotal)
        formatted_service_charge = "£{:.2f}".format(gratuity)
        formatted_total = "£{:.2f}".format(total)

        # Return the result as a dictionary
        result = {
            "Sub Total": formatted_subtotal,
            "Service Charge": formatted_service_charge,
            "Total": formatted_total
        }

        return result


    def split_bill(self):
        pass

