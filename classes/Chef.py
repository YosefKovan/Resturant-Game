
from classes.Staff import Staff

class Chef(Staff):

    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.specialty = 'Italian'

    def cook_order(self, order):
        order.set_status('cooking')
        order.set_status('ready')

    def work(self):
        print("Chef is working!")
        self.energy -= 15


