

class Order:

    def __init__(self, customer, order_number):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = 'pending'
        self.total_price = 0

    def add_item(self, menu_item):
        self.items.append(menu_item)
        self.total_price += menu_item.price

    def remove_item(self, menu_item):

        for index, item in enumerate(self.items):
            if item.name == menu_item.name:
                self.items.pop(index)
                self.total_price -= item.price
                break

    def get_total(self):
        return self.total_price

    def set_status(self, new_status):
        self.status = new_status

    def display_order(self):

        print("Order Details")
        print(f"{self.order_number} {self.customer} {self.status}")
        print("Order Items")

        for item in self.items:
            print(item.get_info())

    def is_complete(self):
        return self.status == 'delivered'