class Fish:
    def __init__(self, name, location, catch_chance, available_times, available_seasons, level_requirement=1):
        self.name = name
        self.location = location
        self.catch_chance = catch_chance
        self.available_times = available_times
        self.available_seasons = available_seasons
        self.level_requirement = level_requirement

    def __str__(self):
        return self.name
