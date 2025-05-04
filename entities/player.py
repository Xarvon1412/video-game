from random import randint
import json

class Entity_Base:
    def __init__(self, name, health, speed):
        self.name = name
        self.health = health
        self.speed = speed

class CreatureFactory:
    @staticmethod
    def load_creature_data(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def create_creature(creature_type, creature_data_file):
        if creature_type in creature_data_file:
            data = creature_data_file[creature_type]

            name = data['name']
            health = randint(data['health_range']['min'], data['health_range']['max'])
            speed = randint(data['speed_range']['min'], data['speed_range']['max'])

            return Entity_Base(name, health, speed)
    
        else:
            print(f"Entity type {creature_type} not found.")
            return None
    
    def attack(self, defending_creature):
        pass

class Player:
    pass

entity_stats = CreatureFactory.load_creature_data('/data/data/com.termux/files/home/projects/video_game/entities/creature_stats.json')

goblin = CreatureFactory.create_creature('goblin', entity_stats)

print(goblin.name, goblin.health, goblin.speed)
print(goblin)
