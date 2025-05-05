from room_descriptions import rooms
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
    def render(player_position, room_dict):
        for room in room_dict:
            if player_position.x == room['cords']['x'] and player_position.y == room['cords']['y']:
                print(room['description'])


new_player = Player()

while game_on:
    print((new_player.position.x, new_player.position.y))
    RenderSystem.render(new_player.position, rooms)
    user_input = InputSystem.check_input_type()
    MovementSystem.move(new_player, user_input)

