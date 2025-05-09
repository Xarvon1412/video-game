from movement_system import MovementSystem


class InputSystem:
    commands = {
        "quit": 2,
    }

    @staticmethod
    def check_input_type():
        user_input = input("What do you wanna do?\n").lower()
        if user_input in MovementSystem.direction_map:
            return user_input
        elif user_input == "quit":
            return 2
        else:
            return 3
