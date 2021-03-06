import math
import random

from aggregate import Aggregate
from position import Position

class Field(object):
    """
    A Field represents a rectangular region containing tiles that initially is empty.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either part of the aggregate or not.
    """
    def __init__(self, width, height, seeds = 0):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room is part of the aggregate.

        width: an integer > 0
        height: an integer > 02 *
        seeds: an integer >= 0
        """
        self.width = width
        self.height = height
        self.radius = min(width, height) / float(2)
        self.aggregates = []

        if seeds > 5:
            # Only take the number of seeds less or equal than 5.
            raise ValueError("Number of seeds greater than 5 is not supported.")

        if seeds == 1 or seeds == 5:
            self.aggregates.append(Aggregate(Position(0, 0)))
        if seeds == 2:
            self.aggregates.append(Aggregate(Position(-width / 2, 0)))
            self.aggregates.append(Aggregate(Position(width / 2, 0)))
        if seeds == 3:
            self.aggregates.append(Aggregate(Position(0, 3**0.5 * width / 6)))
            self.aggregates.append(Aggregate(Position(-width / 2, -3**0.5 * width / 12)))
            self.aggregates.append(Aggregate(Position(width / 2, -3**0.5 * width / 12)))
        if seeds == 4 or seeds == 5:
            self.aggregates.append(Aggregate(Position(-width / 2, height / 2)))
            self.aggregates.append(Aggregate(Position(width / 2, height / 2)))
            self.aggregates.append(Aggregate(Position(width / 2, -height / 2)))
            self.aggregates.append(Aggregate(Position(-width / 2, -height / 2)))

    def count(self):
        """
        Return the number of position in the field.

        returns: an int.
        """
        return self.width * self.height

    def countAggregated(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for aggregate in self.aggregates:
            count += aggregate.count()
        return count

    def getRandomPosition(self):
        """
        Return a random position outside the radius of the seed.

        returns: a Position object.
        """
        # Get a random position in polar coordinate
        radius = random.uniform(self.radius, 2 * self.radius);
        angle = random.uniform(0, 360)

        # Return the position in descartes coordinate.
        return Position(radius * math.cos(angle), radius * math.sin(angle))

    def isParticleInField(self, particle):
        """
        Return True if pos is inside the field.

        particle: a Particle object.
        returns: True if particle is in the field, False otherwise.
        """
        x, y = particle.position.x, particle.position.y
        return abs(x) <= self.width / float(2) and abs(y) <= self.height / float(2)

    def isPositionOutsideDoubleRadius(self, position):
        """
        Return True is the pos is outside the double of the radius from the seed

        pos: a Position object
        returns: True if the pos is outside the double of the radius, False otherwise.
        """
        return (2 * self.radius)**2 <= position.x**2 + position.y**2

    def aggregateSize(self):
        """
        Return the size of the aggregate from the center.
        """
        size = 0
        for aggregate in self.aggregates:
            for x in aggregate.particles:
                for y in aggregate.particles[x]:
                    size = max(size, (x**2 + y**2)**0.5)
        return size
