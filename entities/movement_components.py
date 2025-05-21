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
    x: int
    y: int
    name: str = "Velocity"


@dataclass
class Perspective:
    current: bool
    name: str = "Perspective"
