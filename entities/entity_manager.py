from combat_components import Health
from movement_components import Perspective, Position, Velocity
from movement_system import MovementSystem, RenderSystem
from input_system import InputSystem, PlayerControlled
import array
import numpy

STARTING_COMPONENT_COUNT = 5


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

    def view(self, *components):
        smallest_sparse = components[0].entities
        for component in components:
            if len(component.entities) < len(smallest_sparse):
                smallest_sparse = component.entities
            else:
                pass

        shared_entities = set(smallest_sparse)

        for component in components:
            entity_set = set(component.entities)
            shared_entities &= entity_set

        return shared_entities


class SparseSet:
    component_types = []

    def __init__(self, component_type):
        self.type = component_type
        self.sparse = {}
        self.entities = []
        self.components = []
        SparseSet.component_types.append(self)

    def __repr__(self):
        return f"Component: {self.type}"

    def add(self, entity, component):
        if entity not in self.sparse:
            self.sparse[entity] = component
            self.components.append(component)
            self.entities.append(entity)

        elif entity in self.sparse:
            self.sparse[entity] = component
            self.components[entity] = component

    def get(self, entity):
        if entity in self.sparse:
            return self.sparse[entity]


class SparseSetV2:
    component_types = []

    def __init__(self, component_type):
        self.type = component_type
        self.sparse = []
        self.components = numpy.empty(MAX_ENTITIES, dtype="O")
        self.entities = array.array("i")
        SparseSet.component_types.append(self)

    def add(self, entity, component):
        if entity not in self.entities:
            self.entities.append(entity)
            self.components[entity] = component
            self.sparse
            print(numpy.where(self.components == component))


class SparseSetV3:
    def __init__(self, component_type):
        self.type = component_type
        self.next_index = 0
        self.sparse = numpy.empty(STARTING_COMPONENT_COUNT, dtype="int")
        self.components = numpy.empty(STARTING_COMPONENT_COUNT, dtype="O")
        self.entities = numpy.empty(STARTING_COMPONENT_COUNT, dtype="int")

    def add(self, entityid, component_object):
        # Adds index of component and entity into sparse map at index of entity_id
        self.sparse[entityid] = self.next_index

        # Adds component into contiguous array for quick access
        self.components[self.next_index] = component_object

        # Adds entity_id into continguous array as mirror of component array
        self.entities[self.next_index] = entityid

        # Increments index due to array being pre-configured
        self.next_index += 1

        if self.next_index == self.sparse.size:
            self.sparse.resize(self.next_index * 2)
            self.components.resize(self.next_index * 2)
            self.entities.resize(self.next_index * 2)

        print(self.sparse)
        print(self.components)
        print(self.entities)


newSparse = SparseSetV3("Position")
next_entity = 0

while True:
    input()
    newSparse.add(next_entity, Position(x=next_entity, y=0))

    #    print(newSparse.sparse)
    #    print(newSparse.components)
    #    print(newSparse.entities)

    next_entity += 1

# world = World()
# game_on = True
#
# player = world.create_entity()
# enemy = world.create_entity()
# player_two = world.create_entity()
#
# PositionComponents = SparseSet(Position.name)
# PlayerControlledComponents = SparseSet(PlayerControlled.name)
# VelocityComponents = SparseSet(Velocity.name)
# PerspectiveComponents = SparseSet(Perspective.name)
#
# VelocityComponents.add(player, Velocity(x=0, y=0))
# PositionComponents.add(player, Position(x=2, y=3))
# PlayerControlledComponents.add(player, PlayerControlled())
# PerspectiveComponents.add(player, Perspective(current=True))
#
# PositionComponents.add(enemy, Position(x=1, y=1))
#
#
# while game_on:
#    for entity in world.view(
#        PositionComponents.entities, PlayerControlledComponents.entities
#    ):
#        user_input = InputSystem.get_input()
#        if InputSystem.check_input_type(user_input) == 1:
#            VelocityComponents.add(
#                entity,
#                Velocity(
#                    x=InputSystem.direction_map[user_input][0],
#                    y=InputSystem.direction_map[user_input][1],
#                ),
#            )
#            MovementSystem.move(
#                PositionComponents.components[entity],
#                VelocityComponents.components[entity],
#            )
#            for entity in world.view(PerspectiveComponents.entities):
#                if PerspectiveComponents.get(entity).current:
#                    RenderSystem.render(PositionComponents.get(entity))
#        elif InputSystem.check_input_type(user_input) == 2:
#            quit()
#        else:
#            print("Error")
