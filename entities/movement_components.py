from dataclasses import dataclass

@dataclass
class Position:
    name: str = "Position"
    x: int = 0
    y: int = 0
    

@dataclass
class Moveable:
    name: str = "Moveable"
    moveable: bool = True

@dataclass
class Velocity:
    name: str = "Velocity"
    direction: str = "none"
    x: int = direction_map[direction][0]
    y: int = direction_map[direction][1]
