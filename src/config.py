from __future__ import annotations

import os

import pygame

from color import RGB
from descriptor import Descriptor
from sound import Sound
from theme import Theme


class Config:

    themes = Descriptor()
    idx = Descriptor()
    theme = Descriptor()
    font = Descriptor()

    def __init__(self) -> None:
        self.themes = []
        self.__add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont(
            'monospace', 18, bold=True
            )
        self.move_sound = Sound(
            os.path.join('../assets/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('../assets/sounds/capture.wav'))

    def change_theme(self) -> None:
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def __add_themes(self) -> None:
        green = Theme(RGB(234, 235, 200), RGB(119, 154, 88),
                      RGB(244, 247, 116), RGB(172, 195, 51),
                      RGB(200, 100, 100), RGB(200, 70, 70))
        brown = Theme(RGB(235, 209, 166), RGB(165, 117, 80),
                      RGB(245, 234, 100), RGB(209, 185, 59),
                      RGB(200, 100, 100), RGB(200, 70, 70))
        blue = Theme(RGB(229, 228, 200), RGB(60, 95, 135),
                     RGB(123, 187, 227), RGB(43, 119, 191),
                     RGB(200, 100, 100), RGB(200, 70, 70))
        gray = Theme(RGB(120, 119, 118), RGB(86, 85, 84),
                     RGB(99, 126, 143), RGB(82, 102, 128),
                     RGB(200, 100, 100), RGB(200, 70, 70))

        self.themes = [green, brown, blue, gray]
