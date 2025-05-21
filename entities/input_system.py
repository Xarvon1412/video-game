from movement_components import Velocity
from dataclasses import dataclass


class InputSystem:
    direction_map = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
        "none": (0, 0),
    }

    commands = {
        "quit": 2,
    }

    @staticmethod
    def get_input():
        user_input = input("What do you wanna do?\n").lower()
        return user_input

    @staticmethod
    def check_input_type(user_input):
        if user_input in InputSystem.direction_map:
            return 1
        elif user_input == "quit":
            return 2
        else:
            return 3


@dataclass
class PlayerControlled:
    name: str = "PlayerControlled"
