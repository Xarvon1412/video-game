from entity_manager import World, SparseSet
import movement_components
import input_system

world = World()

#Game state:
#0 = Game ended
#1 = Active movement
#2 = Game paused
game_state = 1

player = world.create_entity()

PositionComponents = SparseSet(movement_components.Position.name)
VelocityComponents = SparseSet(movement_components.Velocity.name)
PlayerControllerComponents = SparseSet(input_system.PlayerControlled.name)
PerspectiveComponents = SparseSet(movement_components.Perspective.name)

while game_state == 1:
    for entity in world.view()
