from classes.Staff import Staff
from classes.Order import Order

class Waiter(Staff):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.tips = 0

    def take_order(self, customer, menu):

        menu.display()
        while True:
            user_choice = input("Please choose a item from the menu: (type exit to stop the loop)")

            if user_choice == "exit":
                break

            item = menu.get_item_by_name(user_choice)

            if not item:
                print("please enter a valid item from the menu!")


    def server_order(self, order):
        order.change_status('delivered')

    def receive_tip(self, amount):
        self.tips += amount

    def get_total_earnings(self):
        return self.salary + self.tips