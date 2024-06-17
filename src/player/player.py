from src.player.inventory import Inventory
from src.player.experience import Experience
from src.player.skill_levels import SkillLevels
from src.skills.fishing.handler import FishingHandler

class Player:
    def __init__(self):
        self.inventory = Inventory()
        self.experience = Experience()
        self.skill_levels = SkillLevels()
        self.fishing_handler = FishingHandler(self)
        
    
    def add_to_inventory(self, item):
        self.inventory.add_item(item)

    def fish(self, location):
        return self.fishing_handler.perform_fishing(location)
