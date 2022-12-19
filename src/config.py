from __future__ import annotations

import os

import pygame

from descriptor import Descriptor
from sound import Sound
from theme import Theme


class Config:

    themes = Descriptor()
    idx = Descriptor()
    theme = Descriptor()
    font = Descriptor()

    def __init__(self) -> None:
        self.themes: list[Theme] | Descriptor = []
        self.__add_themes()
        self.idx: int | Descriptor = 0
        self.theme: Theme | Descriptor = self.themes[self.idx]
        self.font: pygame.font.Font | Descriptor = pygame.font.SysFont(
            'monospace', 18, bold=True
            )
        self.move_sound: Sound = Sound(
            os.path.join('../assets/sounds/move.wav'))
        self.capture_sound: Sound = Sound(
            os.path.join('../assets/sounds/capture.wav'))

    def change_theme(self) -> None:
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def __add_themes(self) -> None:
        green: Theme = Theme((234, 235, 200), (119, 154, 88),
                             (244, 247, 116), (172, 195, 51),
                             (200, 100, 100), (200, 70, 70))
        brown: Theme = Theme((235, 209, 166), (165, 117, 80),
                             (245, 234, 100), (209, 185, 59),
                             (200, 100, 100), (200, 70, 70))
        blue: Theme = Theme((229, 228, 200), (60, 95, 135),
                            (123, 187, 227), (43, 119, 191),
                            (200, 100, 100), (200, 70, 70))
        gray: Theme = Theme((120, 119, 118), (86, 85, 84),
                            (99, 126, 143), (82, 102, 128),
                            (200, 100, 100), (200, 70, 70))

        self.themes = [green, brown, blue, gray]
