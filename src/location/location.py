class Location:
    def __init__(self, name, level_requirement=1):
        self.name = name
        self.level_requirement = level_requirement

    def is_available(self, player):
        return player.skill_levels.get_skill_level("Fishing") >= self.level_requirement

    def fish(self, player):
        raise NotImplementedError("Subclasses should implement this method.")
