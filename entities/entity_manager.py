import numpy


class World:
    def __init__(self):
        self.entities = set()
        self.entity_count = 1
        self.component_types = {}

    def create_entity(self) -> int:
        entity_id = self.entity_count
        self.entities.add(entity_id)
        self.entity_count += 1
        return entity_id

    def register_component(self, component):
#Does this need to have an if/else? Maybe it could just be update()
        if component in self.component_types:
            pass
        else:
            self.component_types.update({component.name: SparseSet()})

    def add_component(self, entity, component, component_data):
        self.register_component(component.name)

        self.component_types[component.name].add(entity, component_data)

        print(self.component_types[component.name].get(entity))


    def components_for_entity(self, entity):
        if entity in self.entities:
            pass

    def view(self, *components):
        smallest_entity_list = components[0].entities
        for component in components:
            if len(component.entities) < len(smallest_entity_list):
                smallest_entity_list = component.entities
            else:
                pass

        shared_entities = set(smallest_entity_list)

        for component in components:
            entity_set = set(component.entities)
            shared_entities &= entity_set

        shared_entities.discard(0)
        return shared_entities




class SparseSet:
    component_types = []

    def __init__(self, component_type="fuck"):
        self.type = component_type
        self.size = 1
        self.max_size = 5
        self.sparse = numpy.zeros(self.max_size, dtype="int")
        self.components = numpy.empty(self.max_size, dtype="O")
        self.entities = numpy.zeros(self.max_size, dtype="int")

    def __repr__(self):
        return f"Component: {self.type}"

    def has(self, entity_id):
        return (
            self.sparse[entity_id] >= 1
            and self.sparse[entity_id] < self.size
            and self.entities[self.sparse[entity_id]] == entity_id
        )

    def add(self, entityid, component_object):
        if not self.has(entityid):
            # Adds index of component and entity into sparse map at index of entity_id
            self.sparse[entityid] = self.size

            # Adds component into contiguous array for quick access
            self.components[self.size] = component_object

            # Adds entity_id into continguous array as mirror of component array
            self.entities[self.size] = entityid

            # Increments index due to array being pre-configured
            self.size += 1

            if self.size == self.max_size:
                self.double_sparse_size()
                self.max_size *= 2

        else:
            self.components[self.sparse[entityid]] = component_object

    def double_sparse_size(self):
        self.sparse.resize(self.max_size * 2)
        self.components.resize(self.max_size * 2)
        self.entities.resize(self.max_size * 2)
        

    def remove(self, entity):
        if self.has(entity):
            last_entity = self.entities[self.size - 1]

            self.components[self.sparse[entity]] = self.components[
                self.sparse[last_entity]
            ]
            self.entities[self.sparse[entity]] = self.entities[self.sparse[last_entity]]
            self.sparse[last_entity] = self.sparse[entity]

            self.sparse[entity] = 0
            self.components[self.size - 1] = None
            self.entities[self.size - 1] = 0

            self.size -= 1

        else:
            pass

    def get(self, entityid):
        if self.has(entityid):
            return self.components[self.sparse[entityid]]
        else:
            return None
