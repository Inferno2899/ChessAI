from descriptor import Descriptor
from my_types import RGB


class Color:

    light = Descriptor()
    dark = Descriptor()

    def __init__(self, light: RGB, dark: RGB) -> None:
        self.light = light
        self.dark = dark
