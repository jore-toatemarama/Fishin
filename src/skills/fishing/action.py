import random
import time

from src.skills.fishing.event import FishingEvent
from src.gametime.time_of_day import TimeOfDay
from src.gametime.season import Season

class FishingAction:
    def __init__(self, player, fish_data):
        self.player = player
        self.fish_data = fish_data

    def calculate_success_rate(self, fish):
        base_rate = self.player.skill_levels.get_skill_level("Fishing") * 2
        item_bonus = sum(item.bonus for item in self.player.inventory.items if hasattr(item, 'bonus'))
        total_rate = base_rate + item_bonus + fish.catch_chance
        return min(total_rate, 90)

    def perform_fishing(self):
        time_of_day = TimeOfDay().get_current_time()
        current_season = Season().get_current_season()

        available_fish = [fish for fish in self.fish_data if (
            time_of_day in fish.available_times and
            current_season in fish.available_seasons and
            self.player.skill_levels.get_skill_level("Fishing") >= fish.level_requirement
        )]

        if not available_fish:
            print("No fish available at this time and location.")
            return None

        print("Casting your line...")
        time.sleep(3)  # Simulate casting time

        fish = random.choice(available_fish)
        success_rate = self.calculate_success_rate(fish)
        return FishingEvent(fish, success_rate).initiate_event()