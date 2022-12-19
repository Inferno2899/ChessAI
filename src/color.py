from descriptor import Descriptor


class Color:

    light = Descriptor()
    dark = Descriptor()

    def __init__(self, light: tuple[int, ...], dark: tuple[int, ...]) -> None:
        self.light: tuple[int, ...] | Descriptor = light
        self.dark: tuple[int, ...] | Descriptor = dark
