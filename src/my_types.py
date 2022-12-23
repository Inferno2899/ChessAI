from typing import NamedTuple


class RGB(NamedTuple):
    red: int
    green: int
    blue: int


class MouseCoords(NamedTuple):
    mouseX: int
    mouseY: int
