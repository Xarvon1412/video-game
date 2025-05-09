from movement_system import MovementSystem, RenderSystem
from entity_manager import EntityManager
from input_system import InputSystem
from combat_components import Health

game_on = True
commands = ["quit"]


class Player:
    def __init__(self):
        self.position = Position(x=2, y=3)
        self.health = Health(100)


new_player = Player()
entity_manager = EntityManager()

while game_on:
    entity_manager.create_entity("health", "left arm", "head")
    #    print((new_player.position.x, new_player.position.y))
    RenderSystem.render(new_player.position)
    user_input = InputSystem.check_input_type()
    if user_input == 2:
        quit()
    elif user_input == 3:
        pass
    else:
        MovementSystem.move(new_player, user_input)
