# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
        #prints items in room
    def print_items(self):
        for item in self.items:
            print(f"Found Item: {item.name}, {item.description}")
    def find_item(self, name):
        for item in self.items:
            if item.name.lower() == item.name.lower():
                return item 