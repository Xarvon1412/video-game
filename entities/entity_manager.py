import numpy

STARTING_COMPONENT_COUNT = 5


class World:
    def __init__(self):
        self.entities = set()
        self.entity_count = 0

    def create_entity(self):
        entity_id = self.entity_count
        self.entities.add(entity_id)
        self.entity_count += 1
        return entity_id

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

        shared_entities.discard(-1)
        return shared_entities


class SparseSet:
    component_types = []

    def __init__(self, component_type):
        self.type = component_type
        self.next_index = 0
        self.sparse = numpy.full(shape=STARTING_COMPONENT_COUNT, fill_value=-1, dtype="int")
        self.components = numpy.empty(STARTING_COMPONENT_COUNT, dtype="O")
        self.entities = numpy.full(STARTING_COMPONENT_COUNT, fill_value=-1, dtype="int")

    def __repr__(self):
        return f"Component: {self.type}"

    def add(self, entityid, component_object):
        if entityid not in self.entities:
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

        else:
            self.components[self.sparse[entityid]] = component_object

    def remove(self, entity):
        if entity in self.entities:
            temp = (
                self.sparse[self.entities[self.next_index - 1]],
                self.entities[self.next_index - 1],
                self.components[self.next_index - 1],
            )
#            print(temp)

#            print(self.sparse[self.entities[entity]])
#            print(self.entities[entity])
#            print(self.components[entity])



            self.entities[entity] = temp[0]
            self.components[entity] = temp[1]

#            print(self.sparse[self.entities[entity]])
#            print(self.entities[entity])
#            print(self.components[entity])



        else:
            pass

    def get(self, entityid):
        if entityid in self.entities:
            return self.components[self.sparse[entityid]]
        else:
            return None
