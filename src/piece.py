import os
from typing import Any, Literal, Optional

from descriptor import Descriptor
from move import Move


class Piece:

    name = Descriptor()
    color = Descriptor()
    color = Descriptor()
    value = Descriptor()
    moves = Descriptor()
    moved = Descriptor()
    texture = Descriptor()
    texture_rect = Descriptor()

    def __init__(self, name: str, color: Literal["white", "black"],
                 value: float, texture: Any = None,
                 texture_rect: Any = None) -> None:
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size: int = 80) -> None:
        self.texture = os.path.join(
            f'../assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_move(self, move: Move) -> None:
        self.moves.append(move)

    def clear_moves(self) -> None:
        self.moves = []


class Pawn(Piece):

    def __init__(self, color: Literal["white", "black"]) -> None:
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)


class Knight(Piece):

    def __init__(self, color: Literal["white", "black"]) -> None:
        super().__init__('knight', color, 3.0)


class Bishop(Piece):

    def __init__(self, color: Literal["white", "black"]) -> None:
        super().__init__('bishop', color, 3.001)


class Rook(Piece):

    def __init__(self, color: Literal["white", "black"]) -> None:
        super().__init__('rook', color, 5.0)


class Queen(Piece):

    def __init__(self, color: Literal["white", "black"]) -> None:
        super().__init__('queen', color, 9.0)


class King(Piece):

    def __init__(self, color: Literal["white", "black"]) -> None:
        self.left_rook: Optional[Rook] = None
        self.right_rook: Optional[Rook] = None
        super().__init__('king', color, 10000.0)
