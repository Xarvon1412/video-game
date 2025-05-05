from dataclasses import dataclass, field

directions = ["up", "down", "left", "right"]
#directions = {
#    'vertical' : {
#        'up': MovementSystem.up(),
#        'down': MovementSystem.down(),
#    },
#    'horizontal' : {
#        'left' : MovementSystem.left(),
#        'right' : MovementSystem.right(),
#    }
#}
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


class MovementSystem:
    direction_map = {
        'up' : lambda y : y - 1,
        'down' : lambda y : y + 1,
        'left' : lambda x : x - 1,
        'right' : lambda x : x + 1,
    }
        
    @staticmethod
    def move(object_moving, direction):
        if direction in MovementSystem.direction_map:
            object_moving.position.x, object_moving.position.y = MovementSystem.direction_map[direction](object_moving.position.x), MovementSystem.direction_map[direction](object_moving.position.y)

class InputSystem:
    @staticmethod
    def check_input_type():
        user_input = input("What do you wanna do?\n").lower()
        if user_input in directions:
            return user_input
        elif user_input in commands:
            return None
        else:
            return None


class RenderSystem:
    @staticmethod
    def render(player_position):
        pass


new_player = Player()

print((new_player.position.x, new_player.position.y))
# InputSystem.obtain_direction()

user_input = InputSystem.check_input_type()
MovementSystem.move(new_player, user_input)
print((new_player.position.x, new_player.position.y))
