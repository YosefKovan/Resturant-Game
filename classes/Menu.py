
class Menu:

    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def remove_item(self, item_name):

        for index, item in enumerate(self.items):
            if item.name == item_name:
                self.items.pop(index)
                break

    def get_item_by_name(self, name):

        for item in self.items:
            if item.name == name:
                return item

        return None

    def get_item_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def display_menu(self):

        print("Printing all items:")
        for item in self.items:
            print(item.get_info())

    def get_total_items(self):
        return len(self.items)





