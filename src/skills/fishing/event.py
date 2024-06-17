import random

class FishingEvent:
    def __init__(self, fish, success_rate):
        self.fish = fish
        self.success_rate = success_rate

    def initiate_event(self):
        print("A fish is biting! Press 'f' to pull it in!")

        user_input = input("Press 'f' to pull: ")
        if user_input.lower() == 'f':
            return self.check_success()
        else:
            print("You missed the fish...")
            return None

    def check_success(self):
        success_roll = random.randint(1, 100)
        if success_roll <= self.success_rate:
            print("You successfully caught the fish!")
            return self.fish
        else:
            print("The fish got away...")
            return None
