from src.location.location import Location
from src.items.fish.fish_data import FishData
from src.skills.fishing.action import FishingAction

class River(Location):
    def __init__(self):
        super().__init__("River", level_requirement=5)

    def fish(self, player):
        action = FishingAction(player, FishData.get_river_fish())
        return action.perform_fishing()
