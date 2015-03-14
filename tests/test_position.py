from classes import *

class TestPosition:

    def test_basic(self):
        p = Position(0.2, 1.5)
        assert p.x == 0.2
        assert p.y == 1.5

    def test_new_position(self):
        p = Position(0.2, 1.5)
        new_p = p.getNewPosition(90, 3)
        assert str(new_p) == "(3.20, 1.50)"

    def test_distance(self):
        p = Position(0.2, 1.5)
        d = p.distance(Position(3.2, 5.5))
        assert d == 5
