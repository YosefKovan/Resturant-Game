
class Staff:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self):
        print("Working")
        self.energy -= 10

    def rest(self):

        if self.energy + 20 > 100:
           self.energy = 100
        else:
            self.energy += 20

    def is_tired(self):
        return self.energy < 30

    def get_info(self):
        return f"Name : {self.name}, Salary : {self.salary}, Energy : {self.energy}"
