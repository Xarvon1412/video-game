from combat_components import Health
from movement_components import Position, Moveable
from movement_system import MovementSystem
from input_system import InputSystem


class World:
    def __init__(self):
        self.entities = set()
        self.entity_count = 0
        self.component_map = {}

    def create_entity(self):
        entity_id = self.entity_count
        self.entities.add(entity_id)
        self.entity_count += 1
        return entity_id

    def components_for_entity(self, entity):
        if entity in self.entities:
            pass

    def view(self, *sparse_sets):
        #        common_entities = zip(sparse_sets)
        #        common_entities = set()
        #        for sparse_set in sparse_sets:
        #            common_entities &= set(sparse_set)
        #        print(list(common_entities))
        smallest_sparse_set = []

        for sparse_set in sparse_sets:
            

        for sparse in sparse_sets:
            sparse = set(sparse)
            shared_entities &= sparse

        print(shared_entities)


class SparseSet:
    component_types = []

    def __init__(self, component):
        self.type = component
        self.sparse = {}
        self.entities = []
        self.components = []
        SparseSet.component_types.append(self)

    def add(self, entity, component):
        if entity not in self.sparse:
            self.sparse[entity] = component
            self.components.append(component)
            self.entities.append(entity)

    def get(self, entity):
        if entity in self.sparse:
            return self.sparse[entity]


world = World()

player = world.create_entity()
enemy = world.create_entity()

PositionComponents = SparseSet(Position.name)
PlayerControlledComponents = SparseSet(Moveable.name)

PositionComponents.add(player, Position(x=2, y=3))
PlayerControlledComponents.add(player, Moveable())
PositionComponents.add(enemy, Position(x=1, y=1))

print(PositionComponents.get(player))

for entity in PlayerControlledComponents.entities:
    MovementSystem.move(PositionComponents.components[entity], "up")

print(PositionComponents.get(player))

for component_type in SparseSet.component_types:
    print(component_type.components)


world.view(PositionComponents.entities, PlayerControlledComponents.entities)
