from classes.Menu import Menu
from classes.Chef import Chef
from classes.Waiter import Waiter
from classes.Order import Order

class Resturant:


    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.staff = []
        self.orders = []
        self.money = 1000
        self.order_number = 0


    def hire_staff(self, staff_member):
        self.staff.append(staff_member)

    def fire_staff(self, staff_name):

        for index, staff in enumerate(self.staff):
            if staff_name == staff.name:
                self.staff.pop(index)
                break

    def create_order(self, customer):

        self.order_number += 1
        self.orders.append(Order(customer, self.order_number))

    def process_order(self, order):

        cook = None
        waiter = None

        for staff in self.staff:
            if isinstance(staff, Chef) and not cook:
                cook = staff
            elif isinstance(staff, Waiter) and not waiter:
                waiter = staff

        if not cook or not waiter:
            print("Cook or waiter not hired yet cannot deliver")
            return

        cook.cook_order(order)
        waiter.server_order(order)

    def complete_order(self, order):
        self.orders.remove(order)
        self.money += order.get_total()

    def pay_salaries(self):

        for staff in self.staff:
            self.money -= staff.salary

    def def_get_statistics(self):
        return {
            "total orders" : self.orders,
            "money" : self.money,
            "staff count" : len(self.staff)
        }

    def display_status(self):
        print(f"name : {self.name}, money :  {self.money}, orders : {self.orders}, staff :  {self.staff}")

    def game_loop(self):

        while True:
            user_input = int(input("Please enter 1 - take order, 2 - view orders, 3 - manage staff, 4 - view stats, 5 - end day"))

            match user_input:
                case 1 :







