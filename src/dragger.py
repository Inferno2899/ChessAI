from typing import Any

import pygame
from pygame.surface import Surface

from const import SQSIZE
from descriptor import Descriptor


class Dragger:

    piece = Descriptor()
    dragging = Descriptor()
    mouseX = Descriptor()
    mouseY = Descriptor()
    initial_row = Descriptor()
    initial_col = Descriptor()

    def __init__(self) -> None:
        self.piece: Any = None
        self.dragging: bool | Descriptor = False
        self.mouseX: int | Descriptor = 0
        self.mouseY: int | Descriptor = 0
        self.initial_row: int | Descriptor = 0
        self.initial_col: int | Descriptor = 0

    # blit method

    def update_blit(self, surface: Surface) -> None:
        # texture
        self.piece.set_texture(size=128)
        texture: Any = self.piece.texture
        # img
        img: Surface = pygame.image.load(texture)
        # rect
        img_center: tuple[int, int] = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.texture_rect)

    # other methods

    def update_mouse(self, pos: tuple[int, ...]) -> None:
        self.mouseX, self.mouseY = pos  # (xcor, ycor)

    def save_initial(self, pos: tuple[int, ...]) -> None:
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece: Any) -> None:
        self.piece = piece
        self.dragging = True

    def undrag_piece(self) -> None:
        self.piece = None
        self.dragging = False
