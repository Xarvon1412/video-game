from combat_components import Health
from movement_components import Position
from movement_system import MovementSystem


class EntityManager:
    def __init__(self):
        self.entities = set()
        self.entity_count = 0
        self.component_map = {}

    #        self.components = {}

    def create_entity(self):
        entity_id = self.entity_count
        self.entities.add(entity_id)
        self.entity_count += 1
        return entity_id

    def add_component(self, entity_id, component, component_type):
        self.component_type = []
        self.component_type.append(component)
        #        self.components[component_type] = []
        #        self.components[component_type].append(component_type)
        self.component_map[component_type] = [entity_id]

    def update(self):
        for component in self.component_map:
            if component == "player_controlled":
                pass


new_manager = EntityManager()

player = new_manager.create_entity()

new_manager.add_component(player, Health(100), Health.component)
new_manager.add_component(player, Health(200), Health)

print(new_manager.component_map)
