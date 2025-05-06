from room_descriptions import rooms
from uuid import uuid4
game_on = True
commands = ["quit"]

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Health:
    def __init__(self, health):
        self.health = health

class Player:
    def __init__(self):
        self.position = Position(x=2, y=3)
        self.health = Health(100)

class EntityManager:
    def __init__(self):
        self.entities = set()

    def create_entity(self, *components):
        new_entity = {}
        entity_id = uuid4()
        new_entity.update({entity_id: list(components)})


class MovementSystem:
    direction_map = {
        'up' : (0, -1),
        'down' : (0, 1),
        'left' : (-1, 0),
        'right' : (1, 0),
    }
        
    @staticmethod
    def move(object_moving, direction):
        if direction in MovementSystem.direction_map:
            object_moving.position.x += MovementSystem.direction_map[direction][0]
            object_moving.position.y += MovementSystem.direction_map[direction][1]

class InputSystem:
    @staticmethod
    def check_input_type():
        user_input = input("What do you wanna do?\n").lower()
        if user_input in MovementSystem.direction_map:
            return user_input
        elif user_input in commands:
            global game_on
            game_on = False
        else:
            game_on = False

class RenderSystem:
    @staticmethod
    def render(player_position):
        for room in rooms.values():
            if player_position.x == room['coords']['x'] and player_position.y == room['coords']['y']:
                print(room['description'])
                return
        print("Huh. You shouldn't be here. Don't know how you got out of bounds, but you should probably go back")


new_player = Player()
entity_manager = EntityManager()

while game_on:
    entity_manager.create_entity('health', 'left arm', 'head')
    id = uuid4()
    print(id)
    #    print((new_player.position.x, new_player.position.y))
    RenderSystem.render(new_player.position)
    user_input = InputSystem.check_input_type()
    MovementSystem.move(new_player, user_input)

