from dataclasses import dataclass, field

game_on = True
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
        if user_input in directions:
            return user_input
        elif user_input in commands:
            global game_on
            game_on = False
        else:
            game_on = False


class RenderSystem:
    @staticmethod
    def render(player_position):
        pass

new_player = Player()

while game_on:
    print((new_player.position.x, new_player.position.y))
    user_input = InputSystem.check_input_type()
    MovementSystem.move(new_player, user_input)

