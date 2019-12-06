class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        def on_take():
            print(f'You have picked up the {self.name}')
        
        def on_drop():
            print(f'You hav dropped the {self.name}')