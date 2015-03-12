import random

from position import Position

class Field(object):
    """
    A Field represents a rectangular region containing tiles tha initially is empty.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either part of the aggregate or not.
    """
    def __init__(self, width, height, seeds = 0):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room is part of the aggregate.

        width: an integer > 0
        height: an integer > 0
        seeds: an integer >= 0
        """
        self.width = width
        self.height = height
        self.tiles = [[False] * height for x in range(width)]

        # Generate the seeds
        for i in range(0, seeds):
            self.aggregateTileAtPosition(Position(width / 2, height / 2))

    def aggregateTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.tiles[int(pos.x)][int(pos.y)] = True

    def isTileAggregated(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[m][n]

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumAggregatedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for line in self.tiles:
            for title in line:
                if title:
                    count += 1
        return count

    def getRandomPosition(self, radius = 0):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x, y  = random.uniform(0, self.width), random.uniform(0, self.height)
        while (x**2 + y**2 < radius**2):
            x, y  = random.uniform(0, self.width), random.uniform(0, self.height)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return 0 <= pos.x and pos.x < self.width and 0 <= pos.y and pos.y < self.height

    def isPositionNextToAggregate(self, pos):
        """
        Return True if pos is next to an aggregated tile.

        pos: a Position object
        returns: True if pos is next to an aggregated tile, False otherwise.
        """
        # Test all adjacent positions.
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # Return True as soon as it finds an aggregated tile.
                p = Position(pos.x + i, pos.y + j)
                if self.isPositionInRoom(p) and self.isTileAggregated(int(p.x), int(p.y)):
                    return True

        return False
