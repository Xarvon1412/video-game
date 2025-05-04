directions = ["up", "down", "left", "right"]
commands = ["quit"]


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_position = (self.x, self.y)


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
        if hasattr(object_moving, "position"):
            object_moving.position.y = getattr(MovementSystem, direction, object_moving)

    #            object_moving.position.x = locals()[direction](object_moving.position.x)


class InputSystem:
    @staticmethod
    def obtain_direction():
        user_direction = input("Please input a direction: ")
        return user_direction.lower()

    @staticmethod
    def check_input_type():
        user_input = input("What do you wanna do?").lower()
        if user_input in directions:
            return user_input
        elif user_input in commands:
            pass
        else:
            pass


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
