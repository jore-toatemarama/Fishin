class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return ', '.join(str(item) for item in self.items)
