# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

        # add to inventory
    def add_to_inventory(self, item):
            self.inventory.append(item)
        
    def remove_from_inventory(self, item):
            self.inventory.remove(item)
        
