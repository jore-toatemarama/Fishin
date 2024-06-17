from src.items.fish.fish import Fish

class FishData:
    @staticmethod
    def get_pond_fish():
        return [
            Fish("Small Fish", "Pond", 50, range(6, 20), ["spring", "summer"], level_requirement=1),
            Fish("Medium Fish", "Pond", 30, range(18, 24), ["summer", "fall"], level_requirement=3),
            Fish("Large Fish", "Pond", 10, range(0, 6), ["winter", "spring"], level_requirement=5)
        ]

    @staticmethod
    def get_river_fish():
        return [
            Fish("River Fish 1", "River", 60, range(5, 19), ["spring", "summer"], level_requirement=5),
            Fish("River Fish 2", "River", 25, range(17, 23), ["summer", "fall"], level_requirement=7),
            Fish("River Fish 3", "River", 15, range(1, 7), ["winter", "spring"], level_requirement=10)
        ]

    @staticmethod
    def get_lake_fish():
        return [
            Fish("Lake Fish 1", "Lake", 50, range(6, 20), ["spring", "summer"], level_requirement=10),
            Fish("Lake Fish 2", "Lake", 30, range(18, 24), ["summer", "fall"], level_requirement=12),
            Fish("Lake Fish 3", "Lake", 10, range(0, 6), ["winter", "spring"], level_requirement=15)
        ]
