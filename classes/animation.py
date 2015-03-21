import math
import time

from Tkinter import *

class Animation:

    def __init__(self, width, height, delay = 0.2):
        """
        Initializes a visualization with the specified parameters.
        """
        # Number of seconds to pause after each frame
        self.delay = delay

        # Initialize a drawing surface
        self.master = Tk()
        self.master.wm_title("pyDLA")
        self.w = Canvas(self.master, width = 500, height = 500)
        self.w.pack()
        self.master.update()

        # Initialize the dimension
        self.init(width, height)

        # Draw some status text
        self.particles = None
        self.text = self.w.create_text(25, 0, anchor = NW, text = self._status_string(0, 0, 0, 0))

        # Update the drawing
        self.master.update()

    def _status_string(self, steps, current, count, num_aggregated_tiles):
        """
        Returns an appropriate status string to print.
        """
        if not num_aggregated_tiles == None:
            self.num_aggregated_tiles = num_aggregated_tiles
        return "Time: %04d; %d particles of a total of %d particles (current: %d)" % \
            (steps, self.num_aggregated_tiles, count, current)

    def _map_coords(self, x, y):
        """
        Maps grid positions to window positions (in pixels).
        """
        return (250 + 450 * (x / float(self.max_dim)),
                250 + 450 * (-y / float(self.max_dim)))

    def init(self, width, height):
        """
        Init the grid with the given dimension.
        """
        # Update the size of the field
        self.width = width
        self.height = height
        self.max_dim = max(width, height)

        # Draw a backing and lines
        x1, y1 = self._map_coords(-width / 2, height / 2)
        x2, y2 = self._map_coords(width / 2, -height / 2)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

    def update(self, steps, current, count, field = None):
        """
        Redraws the visualization with the specified field and particles state.
        """

        if not field == None:
            # Display the aggregates

            if self.particles:
                # Remove the aggregates
                for particle in self.particles:
                    self.w.delete(particle)

            # Display the aggregate.
            self.particles = []
            for aggregate in field.aggregates:
                for x in aggregate.particles:
                    for y in aggregate.particles[x]:
                        x1, y1 = self._map_coords(x, y)
                        x2, y2 = self._map_coords(x + 1, y + 1)
                        self.particles.append(self.w.create_rectangle(x1, y1, x2, y2, fill = 'black'))

        # Update text
        self.w.delete(self.text)
        count_aggregated = field.countAggregated() if not field == None else None
        text = self._status_string(steps, current, count, count_aggregated)
        self.text = self.w.create_text(25, 0, anchor= NW, text = text)

        # Update the canvas
        self.master.update()
        time.sleep(self.delay)

    def done(self):
        """
        Indicate that the animation is done so that we allow the user to close the window.
        """
        mainloop()
