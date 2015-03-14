import random

from classes import *

class TestParticle:

    def test_basic(self):
        f = Field(10, 10)
        p = Particle(f, 1)
        assert 0 <= p.direction and p.direction <= 360
        assert f.isPositionInRoom(p.position)
        assert p.valid

    def test_standard(self):
        f = Field(10, 10)
        # Set a aggregated position.
        f.aggregateTileAtPosition(Position(8, 7))
        assert f.isTileAggregated(8, 7)
        # Set a particule close to the aggregated position
        # and test it will aggregate.
        p = StandardParticle(f, 1)
        p.position = Position(8, 6)
        p.aggregate()
        assert f.isTileAggregated(8, 6)
