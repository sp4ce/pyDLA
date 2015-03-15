from position import Position
from particle import Particle

class Aggregate:
    """
    Define an aggregate
    """

    def __init__(self, radius,  seed = Position(0, 0)):
        """
        Initialize an aggregate with the given seed position.

        radius: a float
        seed: a Position, by default in the (0, 0)
        """
        self.seed = seed
        self.radius = radius
        self.particles = {int(seed.x) : { int(seed.y): True }}

    def contains(self, position):
        """
        Test if the aggregate contains the given position.

        position: a Position, the position tho test.
        """
        if not int(position.x) in self.particles:
            return False
        else:
            return int(position.y) in self.particles[int(position.x)]

    def add(self, position):
        """
        Aggregate the particle to the aggregate.

        position: a Position, the position of the particle.
        """
        if not int(position.x) in self.particles:
            self.particles[int(position.x)] = { int(position.y): True }
        elif not int(position.y) in self.particles[int(position.x)]:
            self.particles[int(position.x)][int(position.y)] = True

    def isAdjacent(self, position):
        """
        Return true if the particle is adjacent to the aggregate.

        position: a Position, the position of the particle
        returns: True if the particle is adjacent to the aggregate, False otherwise.
        """
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    # Do not test the current position.
                    continue
                # Return True as soon as it finds an aggregated position.
                if self.contains(Position(position.x + i, position.y + j)):
                    return True
        return False

    def count(self):
        """
        Return the number of aggregated particles

        returns: int, the number of particles in the aggregats
        """
        count = 0
        for x in self.particles:
            count += len(self.particles[x])
        return count

    def size(self):
        """
        Return the size of the aggregate from the seeds.

        returns: a float, the distance from the seed.
        """
        size = 0
        for x in self.particles:
            for y in self.particles[x]:
                size = max(size, self.seed.distance(Position(x, y)))
        return size
