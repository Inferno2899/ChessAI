from __future__ import annotations

from descriptor import Descriptor
from square import Square


class Move:

    initial = Descriptor()
    final = Descriptor()

    def __init__(self, initial: Square, final: Square) -> None:
        # initial and final are squares
        self.initial = initial
        self.final = final

    def __str__(self) -> str:
        s: str = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Move):
            return self.initial == other.initial and self.final == other.final
        else:
            raise NotImplementedError
