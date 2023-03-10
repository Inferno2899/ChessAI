from __future__ import annotations

from typing import Final, Literal, Optional

from descriptor import Descriptor
from piece import Piece


class Square:

    row = Descriptor()
    col = Descriptor()
    piece = Descriptor()
    alphacol = Descriptor()

    __ALPHACOLS: Final = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h'
    }

    def __init__(self, row: int, col: int,
                 piece: Optional[Piece] = None) -> None:
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.__ALPHACOLS[self.col]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Square):
            return self.row == other.row and self.col == other.col
        else:
            raise NotImplementedError

    def has_piece(self) -> bool:
        return self.piece is not None

    def isempty(self) -> bool:
        return not self.has_piece()

    def has_team_piece(self, color: Literal["white", "black"]) -> bool:
        return self.has_piece() and self.piece.color == color

    def has_enemy_piece(self, color: Literal["white", "black"]) -> bool:
        return self.has_piece() and self.piece.color != color

    def isempty_or_enemy(self, color: Literal["white", "black"]) -> bool:
        return self.isempty() or self.has_enemy_piece(color)

    @staticmethod
    def in_range(*args: int) -> bool:
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True

    @classmethod
    def get_alphacol(cls, col: int) -> str:
        return cls.__ALPHACOLS[col]
