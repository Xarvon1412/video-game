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
    @staticmethod
    def up(y):
        return y - 1

    @staticmethod
    def down(y):
        return y + 1

    @staticmethod
    def left(x):
        return x - 1

    @staticmethod
    def right(x):
        return x + 1

    @staticmethod
    def move(object_moving, direction):
        if direction == 'up' or direction == 'down':
            object_moving.position.y = getattr(MovementSystem, direction)(object_moving.position.y)

        if direction == 'left' or direction == 'right':
            object_moving.position.x = getattr(MovementSystem,direction)(object_moving.position.x)
#        if direction == 'up':
#           object_moving.position.y = MovementSystem.up(object_moving.position.y)
#      if direction = 'down':



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
