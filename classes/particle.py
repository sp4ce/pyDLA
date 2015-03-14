import random

class Particle(object):
    """
    Represents a Particle moving into the field.

    At all times the particle has a particular position and direction in the room.
    The particle also has a fixed speed.

    Subclasses of Particle should provide movement strategies by implementing
    updatePositionAndAggregate(), which simulates a single time-step.s
    """
    def __init__(self, field, speed):
        """
        Initializes a Particle with the given speed in the specified field. The
        particle initially has a random direction and a random position in the
        room.

        field:  a Field object.
        speed: a float (speed > 0)
        """
        self.field = field
        self.speed = speed
        self.position = field.getRandomPosition()
        self.direction = random.randint(0, 360)
        self.valid = True
        self.aggregated = False

    def updatePositionAndAggregate(self):
        """
        Simulate the raise passage of a single time-step.

        Move the particle to a new position.
        """
        self.updatePosition()
        self.aggregate()

    def updatePosition(self):
        raise NotImplementedError # don't change this!

    def aggregate(self):
        raise NotImplementedError # don't change this!


class StandardParticle(Particle):
    """
    A StandardParticle is a Particle with the standard movement strategy.

    It chooses a new direction at random at the end of each time-step and it aggregates
    each time it is in contact with the aggregate.
    """
    def updatePosition(self):
        # Update the position
        self.direction = random.randint(0, 360)
        self.position = self.position.getNewPosition(self.direction, self.speed)

        # If the particle move outside the room, just reject it.
        if self.field.isPositionOutsideDoubleRadius(self.position):
            self.valid = False

    def aggregate(self):
        # If the particle is next to the aggregate, aggregate it.
        for aggregate in self.field.aggregates:
            if aggregate.isAdjacent(self.position):
                aggregate.add(self.position)
                self.aggregated = True
                return
