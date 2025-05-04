import json

class Entity_Base:
    def __init__():
        self.health = None
        self.name = None
        self.speed = None

    @staticmethod
    def load_stats(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @classmethod
    def create_entity(cls, entity_type, stats_file):
        if entity_type in stats_file:
            data = stats_file[entity_type]

        else:
            print("Yo, that doesn't exist.")

    def attack(self):
        pass

class Goblin(Entity_Base, name):
    def __init__(self):
        super().__init__()

entity_stats = Entity_Base.load_stats('creature_stats.json')

#new_goblin = Entity_Base.create_entity("goblin", entity_stats)

print(entity_stats)
