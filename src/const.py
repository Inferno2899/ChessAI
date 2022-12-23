from typing import Final, Literal

# Screen dimensions
WIDTH: Final[Literal[800]] = 800
HEIGHT: Final[Literal[800]] = 800

# Board dimensions
ROWS: Final[Literal[8]] = 8
COLS: Final[Literal[8]] = 8
SQSIZE: Final[int] = WIDTH // COLS

# Frames per second
FPS: Final[Literal[30]] = 30
