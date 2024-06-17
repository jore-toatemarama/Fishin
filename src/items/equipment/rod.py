class FishingRod:
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus

    def __str__(self):
        return self.name