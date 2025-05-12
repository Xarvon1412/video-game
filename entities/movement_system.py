from room_descriptions import rooms


class MovementSystem:
    direction_map = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    @staticmethod
    def move(object_moving, direction):
        if direction in MovementSystem.direction_map:
            object_moving.x += MovementSystem.direction_map[direction][0]
            object_moving.y += MovementSystem.direction_map[direction][1]


class RenderSystem:
    @staticmethod
    def render(player_position):
        for room in rooms.values():
            if (
                player_position.x == room["coords"]["x"]
                and player_position.y == room["coords"]["y"]
            ):
                print(room["description"])
                return
        print(
            "Huh. You shouldn't be here. Don't know how you got out of bounds, but you should probably go back"
        )
