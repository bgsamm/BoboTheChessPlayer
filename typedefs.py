from __future__ import annotations

from enum import Enum


class PieceChar(Enum):
    """FEN characters for each piece"""

    KING = 'k'
    QUEEN = 'q'
    BISHOP = 'b'
    KNIGHT = 'n'
    ROOK = 'r'
    PAWN = 'p'

    def __str__(self):
        pieceNames = {
            PieceChar.KING: 'king',
            PieceChar.QUEEN: 'queen',
            PieceChar.BISHOP: 'bishop',
            PieceChar.KNIGHT: 'knight',
            PieceChar.ROOK: 'rook',
            PieceChar.PAWN: 'pawn'
        }
        return pieceNames[self]


class ColorChar(Enum):
    """FEN characters for the piece colors"""

    WHITE = 'w'
    BLACK = 'b'

    @property
    def opponent(self) -> ColorChar:
        """Returns this color's opposing color"""

        return ColorChar.BLACK if self == ColorChar.WHITE else ColorChar.WHITE

    def __str__(self):
        colorNames = {
            ColorChar.WHITE: 'white',
            ColorChar.BLACK: 'black'
        }
        return colorNames[self]


ColorRGB = tuple[int, int, int]
"""A color represented by a (red, green, blue) tuple"""

ColorRGBA = tuple[int, int, int, int]
"""A color represented by a (red, green, blue, alpha) tuple"""

Color = (ColorRGB | ColorRGBA)

Coord = tuple[int, int]
"""An (x, y) coordinate pair"""

Size = tuple[int, int]
"""A (width, height) pair"""

NormCoord = tuple[float, float]
"""An (x, y) pair of floats normalized between 0.0 and 1.0"""

Vector = tuple[int, int]
"""A 2-tuple representing a direction"""
