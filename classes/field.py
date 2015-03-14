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

        # Generate the seeds
        # TODO(baptiste): Pattern to generate more then one seed
        # The barycentre of all the seeds should be (0, 0)
        # the radius of all aggregates should be inside the radius of the field.
        self.aggregates = []
        for i in range(0, seeds):
            self.aggregates.append(Aggregate(self.radius))

    def count(self):
        """
        Return the number of position in the field.

        returns: an int.
        """
        return self.width * self.height

    def isAggregated(self, x ,y):
        """
        Test if the given position is aggregated

        x: a float, the position x
        y: a float, the position y
        """
        for aggregate in self.aggregates:
            if (aggregate.contains(Position(x, y))):
                return True
        return False

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
