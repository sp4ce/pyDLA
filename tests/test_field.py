import random

from classes import *

class TestField:

    def test_seeds(self):
        random.seed(0)
        f = Field(10, 10, 2)
        # We generate only one seed.
        assert f.getNumAggregatedTiles() == 1

    def test_getNumTiles(self):
        f = Field(10, 10)
        assert f.getNumTiles() == 100

    def test_getNumAggregatedTiles(self):
        f = Field(10, 10)
        assert f.getNumAggregatedTiles() == 0

    def test_aggregateTileAtPosition(self):
        f = Field(10, 10)
        f.aggregateTileAtPosition(Position(5.1, 4.9))
        assert f.getNumAggregatedTiles() == 1
        assert f.isTileAggregated(5, 4)

    def test_isPositionNextToAggregate(self):
        f = Field(10, 10)
        p = Position(5.1, 4.9)
        f.aggregateTileAtPosition(p)
        assert f.isPositionNextToAggregate(p)
        assert f.isPositionNextToAggregate(Position(p.x + 1, p.y))
        assert f.isPositionNextToAggregate(Position(p.x, p.y + 1))
