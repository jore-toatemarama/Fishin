from src.location.location import Location
from src.items.fish.fish_data import FishData
from src.skills.fishing.action import FishingAction

class Lake(Location):
    def __init__(self):
        super().__init__("Lake", level_requirement=10)

    def fish(self, player):
        action = FishingAction(player, FishData.get_lake_fish())
        return action.perform_fishing()
