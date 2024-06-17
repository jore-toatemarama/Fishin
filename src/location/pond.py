from src.location.location import Location
from src.items.fish.fish_data import FishData
from src.skills.fishing.action import FishingAction

class Pond(Location):
    def __init__(self):
        super().__init__("Pond")

    def fish(self, player):
        action = FishingAction(player, FishData.get_pond_fish())
        return action.perform_fishing()
