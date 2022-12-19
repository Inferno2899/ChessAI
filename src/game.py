from typing import Any, Literal

import pygame
from pygame.surface import Surface

from board import Board
from config import Config
from const import COLS, HEIGHT, ROWS, SQSIZE
from descriptor import Descriptor
from dragger import Dragger
from square import Square
from theme import Theme


class Game:

    next_player = Descriptor()
    hovered_sqr = Descriptor()
    board = Descriptor()
    dragger = Descriptor()
    config = Descriptor()

    def __init__(self) -> None:
        self.next_player: Literal['white', 'black'] | Descriptor = 'white'
        self.hovered_sqr: Square | None | Descriptor = None
        self.board: Board | Descriptor = Board()
        self.dragger: Dragger | Descriptor = Dragger()
        self.config: Config | Descriptor = Config()

    # blit methods

    def show_bg(self, surface: Surface) -> None:
        theme: Theme = self.config.theme

        for row in range(ROWS):
            for col in range(COLS):
                # color
                color: tuple[int, ...] = (theme.bg.light
                                          if (row + col) % 2 == 0
                                          else theme.bg.dark)
                # rect
                rect: tuple[int, ...] = (col * SQSIZE, row * SQSIZE,
                                         SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

                # row coordinates
                if col == 0:
                    # color
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # label
                    lbl: Surface = self.config.font.render(str(ROWS-row), True,
                                                           color)
                    lbl_pos: tuple[int, ...] = (5, 5 + row * SQSIZE)
                    # blit
                    surface.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = (theme.bg.dark
                             if (row + col) % 2 == 0
                             else theme.bg.light)
                    # label
                    lbl = self.config.font.render(Square.get_alphacol(col),
                                                  True, color)
                    lbl_pos = (col * SQSIZE + SQSIZE - 20, HEIGHT - 20)
                    # blit
                    surface.blit(lbl, lbl_pos)

    def show_pieces(self, surface: Surface) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece: Any = self.board.squares[row][col].piece

                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img: Surface = pygame.image.load(piece.texture)
                        img_center: tuple[int, int] = (col * SQSIZE +
                                                       SQSIZE // 2,
                                                       row * SQSIZE +
                                                       SQSIZE // 2)
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface: Surface) -> None:
        theme: Theme = self.config.theme

        if self.dragger.dragging:
            piece: Any = self.dragger.piece

            # loop all valid moves
            for move in piece.moves:
                # color
                color: tuple[int, ...] = (theme.moves.light if
                                          (move.final.row + move.final.col)
                                          % 2 == 0 else theme.moves.dark)
                # rect
                rect: tuple[int, ...] = (move.final.col * SQSIZE,
                                         move.final.row * SQSIZE,
                                         SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface: Surface) -> None:
        theme: Theme = self.config.theme

        if self.board.last_move:
            initial: Square = self.board.last_move.initial
            final: Square = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color: tuple[int, ...] = (theme.trace.light if
                                          (pos.row + pos.col) % 2 == 0
                                          else theme.trace.dark)
                # rect
                rect: tuple[int, ...] = (pos.col * SQSIZE, pos.row * SQSIZE,
                                         SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface: Surface) -> None:
        if self.hovered_sqr:
            # color
            color: tuple[int, ...] = (180, 180, 180)
            # rect
            rect: tuple[int, ...] = (self.hovered_sqr.col * SQSIZE,
                                     self.hovered_sqr.row * SQSIZE,
                                     SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=3)

    # other methods

    def next_turn(self) -> None:
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row: int, col: int) -> None:
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self) -> None:
        self.config.change_theme()

    def play_sound(self, captured: bool = False) -> None:
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    def reset(self) -> None:
        self.__init__()
