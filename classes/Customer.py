
class Customer:

    def __init__(self, name):
        self.name = name
        self.satisfaction = 50

    def increase_satisfaction(self, amount):

        if 50 <= amount + self.satisfaction <=100:
            self.satisfaction += amount
        else:
            print("Unable to add to the satisfaction out of range!")

    def decrease_satisfaction(self, amount):

        if self.satisfaction - amount >= 0:
            self.satisfaction -= amount

    def  is_happy(self):
        return self.satisfaction > 70

    def get_info(self):
        return f"Customer Name : {self.name},  Satisfaction level : {self.satisfaction}"
