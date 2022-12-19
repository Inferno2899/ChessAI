from color import Color
from descriptor import Descriptor


class Theme:

    bg = Descriptor()
    trace = Descriptor()
    moves = Descriptor()

    def __init__(self, light_bg: tuple[int, ...],
                 dark_bg: tuple[int, ...],
                 light_trace: tuple[int, ...],
                 dark_trace: tuple[int, ...],
                 light_moves: tuple[int, ...],
                 dark_moves: tuple[int, ...]) -> None:

        self.bg: Color | Descriptor = Color(light_bg, dark_bg)
        self.trace: Color | Descriptor = Color(light_trace, dark_trace)
        self.moves: Color | Descriptor = Color(light_moves, dark_moves)
