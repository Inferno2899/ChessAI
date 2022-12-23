from typing import Optional

import pygame
from pygame.surface import Surface

from const import SQSIZE
from descriptor import Descriptor
from my_types import MouseCoords
from piece import Piece


class Dragger:

    piece = Descriptor()
    dragging = Descriptor()
    mouseX = Descriptor()
    mouseY = Descriptor()
    initial_row = Descriptor()
    initial_col = Descriptor()

    def __init__(self) -> None:
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    # blit method

    def update_blit(self, surface: Surface) -> None:
        # texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # img
        img = pygame.image.load(texture)
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.texture_rect)

    # other methods

    def update_mouse(self, pos: MouseCoords) -> None:
        self.mouseX, self.mouseY = pos  # (xcor, ycor)

    def save_initial(self, pos: MouseCoords) -> None:
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece: Optional[Piece]) -> None:
        self.piece = piece
        self.dragging = True

    def undrag_piece(self) -> None:
        self.piece = None
        self.dragging = False
