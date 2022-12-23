from color import RGB, Color
from descriptor import Descriptor


class Theme:

    bg = Descriptor()
    trace = Descriptor()
    moves = Descriptor()

    def __init__(self, light_bg: RGB,
                 dark_bg: RGB,
                 light_trace: RGB,
                 dark_trace: RGB,
                 light_moves: RGB,
                 dark_moves: RGB) -> None:

        self.bg = Color(light_bg, dark_bg)
        self.trace = Color(light_trace, dark_trace)
        self.moves = Color(light_moves, dark_moves)
