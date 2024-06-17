from src.skills.fishing.action import FishingAction

class FishingHandler:
    def __init__(self, player):
        self.player = player

    def perform_fishing(self, location):
        return location.fish(self.player)
