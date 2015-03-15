from classes import *

class TestAggregate:

    def test_init(self):
        aggregate = Aggregate(10)
        assert aggregate.seed.x == 0
        assert aggregate.seed.y == 0
        assert aggregate.particles[0][0]

    def test_add(self):
        aggregate = Aggregate(10)

        position = Position(1, 0)
        aggregate.add(position)
        assert aggregate.particles[1][0]

        position = Position(1.1, 1.9)
        aggregate.add(position)
        assert aggregate.particles[1][1]

    def test_contains(self):
        aggregate = Aggregate(10)

        position = Position(1.3, 0.9)
        aggregate.add(position)
        assert aggregate.contains(Position(1.9, 0.3))

    def test_isAdjacent(self):
        aggregate = Aggregate(10)
        p = Position(5.1, 4.9)
        aggregate.add(p)

        assert not aggregate.isAdjacent(p)
        assert aggregate.isAdjacent(Position(p.x + 1, p.y))
        assert aggregate.isAdjacent(Position(p.x, p.y + 1))

    def test_count(self):
        aggregate = Aggregate(10)
        assert aggregate.count() == 1

        aggregate.add(Position(5.1, 4.9))
        assert aggregate.count() == 2

    def test_size(self):
        aggregate = Aggregate(10)
        assert aggregate.size() == 0

        aggregate.add(Position(3, 4))
        assert aggregate.size() == 5
