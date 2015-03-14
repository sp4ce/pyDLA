import random

from classes import *

class TestField:

    def test_init(self):
        field = Field(10, 10)
        assert field.radius == 5
        field = Field(10, 15)
        assert field.radius == 5
        field = Field(15, 10)
        assert field.radius == 5

    def test_initWithSeed(self):
        field = Field(10, 10, 1)
        assert len(field.aggregates) == 1
        assert field.aggregates[0].radius == 5

    def test_count(sefl):
        field = Field(10, 10)
        assert field.count() == 100

    def test_isAggregated(self):
        field = Field(10, 10, 1)
        assert field.isAggregated(0.5, 0.5)

    def test_countAggregated(self):
        field = Field(10, 10, 1)
        assert field.countAggregated() == 1

    def test_getRandomPosition(self):
        field = Field(10, 10)
        random.seed(0)
        position = field.getRandomPosition()
        assert "(-8.28, 4.05)" == str(position)

    def test_isParticleInField(self):
        field = Field(10, 10)
        p = Particle(field, 1)
        p.position = Position(5, 5)
        assert field.isParticleInField(p)
        p.position = Position(-5, -5)
        assert field.isParticleInField(p)
        p.position = Position(5.1, 5)
        assert not field.isParticleInField(p)
        p.position = Position(5, 5.1)
        assert not field.isParticleInField(p)

    def test_isPositionOutsideDoubleRadius(self):
        field = Field(10, 10)
        assert not field.isPositionOutsideDoubleRadius(Position(0, 9.9))
        assert field.isPositionOutsideDoubleRadius(Position(0, 10))
        assert not field.isPositionOutsideDoubleRadius(Position(9.9, 0))
        assert field.isPositionOutsideDoubleRadius(Position(10, 0))

    def test_aggregateSize(self):
        field = Field(10, 10)
        assert field.aggregateSize() == 0

        field = Field(10, 10, 1)
        field.aggregates[0].add(Position(3, 4))
        assert field.aggregateSize() == 5
