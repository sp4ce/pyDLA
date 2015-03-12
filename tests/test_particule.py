import random

from classes import *

class TestParticule:

    def test_basic(self):
        f = Field(10, 10)
        p = Particule(f, 1)
        assert 0 <= p.direction and p.direction <= 360
        assert f.isPositionInRoom(p.position)
        assert p.valid

    def test_standard(self):
        random.seed(0)
        f = Field(10, 10, 1)
        assert f.isTileAggregated(8, 7)
        p = StandardParticule(f, 1)
        p.position = Position(8, 6)
        p.aggregate()
        assert f.isTileAggregated(8, 6)
