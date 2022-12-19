import pygame

from descriptor import Descriptor


class Sound:

    path = Descriptor()
    sound = Descriptor()

    def __init__(self, path: str) -> None:
        self.path: str | Descriptor = path
        self.sound: pygame.mixer.Sound | Descriptor = \
            pygame.mixer.Sound(self.path)

    def play(self) -> None:
        pygame.mixer.Sound.play(self.sound)
