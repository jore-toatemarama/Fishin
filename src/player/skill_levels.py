class SkillLevels:
    def __init__(self):
        self.levels = {
            "Fishing": 1
        }

    def increase_skill(self, skill, amount):
        if skill in self.levels:
            self.levels[skill] += amount
        else:
            self.levels[skill] = amount

    def get_skill_level(self, skill):
        return self.levels.get(skill, 0)