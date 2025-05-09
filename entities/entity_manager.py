from combat_components import Health
from movement_components import Position


class EntityManager:
    def __init__(self):
        self.entities = set()
        self.entity_count = 0
        self.components = {}

    def create_entity(self):
        entity_id = self.entity_count
        self.entities.add(entity_id)
        self.entity_count += 1

    def add_component(self, entity_id, component_type):
        self.components[component_type][entity_id]
