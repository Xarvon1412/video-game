from entity_manager import World, SparseSet
import movement_components
from input_system import InputSystem, PlayerControlled
from movement_system import MovementSystem, RenderSystem

world = World()

# Game state:
# 0 = Game ended
# 1 = Active movement
# 2 = Game paused
game_on = True
game_state = 1

player1 = world.create_entity()
player2 = world.create_entity()


world.add_component(player1, movement_components.Position(x=0, y=0))
world.add_component(player1, movement_components.Velocity(x=1, y=1))

world.add_component(player2, PlayerControlled())

world.components_for_entity(player1)

#PositionComponents = SparseSet(movement_components.Position.name)
#VelocityComponents = SparseSet(movement_components.Velocity.name)
#PlayerControlledComponents = SparseSet(PlayerControlled.name)
#PerspectiveComponents = SparseSet(movement_components.Perspective.name)
#
#player = world.create_entity()
#PositionComponents.add(player, movement_components.Position(x=1, y=0))
#PlayerControlledComponents.add(player, PlayerControlled())
#
#enemy1 = world.create_entity()
#PositionComponents.add(enemy1, movement_components.Position(x=2, y=0))
#
#player2 = world.create_entity()
#PositionComponents.add(player2, movement_components.Position(x=3, y=0))
#
#player3 = world.create_entity()
#PositionComponents.add(player3, movement_components.Position(x=4, y=0))
#PlayerControlledComponents.add(player3, PlayerControlled())
#
#player4 = world.create_entity()
#PositionComponents.add(player4, movement_components.Position(x=5, y=0))
#
#print(PositionComponents.sparse)
#print(PositionComponents.components)
#print(PositionComponents.entities)
#
#
#PositionComponents.remove(player2)
#
#print(PositionComponents.sparse)
#print(PositionComponents.components)
#print(PositionComponents.entities)

###################################
# while game_on:
#    if game_state == 0:
#        break
#    while game_state == 1:
#        for entity in world.view(PositionComponents, PlayerControlledComponents):
#            user_input = InputSystem.get_input()
#            if InputSystem.check_input_type(user_input) == 1:
#                VelocityComponents.add(
#                    entity,
#                    movement_components.Velocity(
#                        x=InputSystem.direction_map[user_input][0],
#                        y=InputSystem.direction_map[user_input][1],
#                    ),
#                )
#                MovementSystem.move(
#                    PositionComponents.get(entity), VelocityComponents.get(entity)
#                )
#                RenderSystem.render(PositionComponents.get(entity))
#            else:
#                game_state = 0


quit()
