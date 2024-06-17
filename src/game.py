from src.player.player import Player
from src.location.pond import Pond
from src.location.river import River
from src.location.lake import Lake
from src.gametime.time_of_day import TimeOfDay
from src.gametime.season import Season

class Game:
    def __init__(self):
        self.player = Player()
        self.running = True
        self.locations = {
            "POND": Pond(),
            "RIVER": River(),
            "LAKE": Lake()
        }
        self.current_location = self.locations["POND"]

    def select_location(self, location_name):
        location = self.locations.get(location_name)
        if location and location.is_available(self.player):
            self.current_location = location
            print(f"You are now at {self.current_location.name}")
        else:
            print(f"Location '{location_name}' is not available or unknown.")

    def process_input(self, user_input):
        if user_input == "fish":
            fish = self.current_location.fish(self.player)
            if fish:
                print(f"You caught a {fish}!")
                print("Inventory:")
                for item in self.player.inventory.items:
                    print(item)
            else:
                print("No fish available or the fish got away.")
        elif user_input.startswith("go to"):
            location_name = user_input.split(" ")[-1].upper()
            self.select_location(location_name)
        elif user_input == "quit":
            self.running = False
        else:
            print("Unknown command.")

    def run(self):
        print("Welcome to the Fishing Game!")
        while self.running:
            current_time = TimeOfDay().get_current_time()
            current_season = Season().get_current_season()
            print(f"Current Time: {current_time}:00")
            print(f"Current Season: {current_season.capitalize()}")
            print("Commands: 'fish' to fish, 'go to [location]' to change location, 'quit' to exit.")
            print("Available locations: POND, RIVER, LAKE")
            user_input = input("Enter command: ")
            self.process_input(user_input)