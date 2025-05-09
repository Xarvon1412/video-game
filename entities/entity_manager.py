from uuid import uuid4
from combat_components import Health
from movement_components import Position


class EntityManager:
    def __init__(self):
        self.entities = set()
        self.entity_count = 0

    def create_entity(self, *components):
        entity_id = self.entity_count
        self.entity_count += 1
