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
