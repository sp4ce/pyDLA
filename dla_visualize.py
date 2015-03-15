import math
import time

from Tkinter import *

class Visualization:

    def __init__(self, width, height, delay = 0.2):
        """
        Initializes a visualization with the specified parameters.
        """
        # Number of seconds to pause after each frame
        self.delay = delay

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width = 500, height = 500)
        self.w.pack()
        self.master.update()

        # Initialize the dimension
        self.init(width, height)

        # Draw some status text
        self.particles = None
        self.text = self.w.create_text(25, 0, anchor = NW, text = self._status_string(0, 0))
        self.time = 0

        # Update the drawing
        self.master.update()

    def _status_string(self, time, num_aggregated_tiles):
        """
        Returns an appropriate status string to print.
        """
        percent_aggregated = 100 * num_aggregated_tiles / (self.width * self.height)
        return "Time: %04d; %d tiles (%d%%) aggregated" % \
            (time, num_aggregated_tiles, percent_aggregated)

    def _map_coords(self, x, y):
        """
        Maps grid positions to window positions (in pixels).
        """
        return (250 + 450 * (x / float(self.max_dim)),
                250 + 450 * (-y / float(self.max_dim)))

    def _draw_particle(self, position, direction):
        "Returns a polygon representing a particle with the specified parameters."
        x, y = position.x, position.y
        d1 = direction + 165
        d2 = direction - 165
        x1, y1 = self._map_coords(x, y)
        x2, y2 = self._map_coords(x + 0.6 * math.sin(math.radians(d1)),
                                  y + 0.6 * math.cos(math.radians(d1)))
        x3, y3 = self._map_coords(x + 0.6 * math.sin(math.radians(d2)),
                                  y + 0.6 * math.cos(math.radians(d2)))
        return self.w.create_polygon([x1, y1, x2, y2, x3, y3], fill="red")

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

        # Draw gray squares for empty tiles
        self.tiles = {}
        for i in range(-width / 2, width / 2):
            for j in range(-height / 2, height / 2):
                x1, y1 = self._map_coords(i, j)
                x2, y2 = self._map_coords(i + 1, j + 1)
                self.tiles[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2, fill = "gray")

        # Draw gridlines
        for i in range(-width / 2, width / 2):
            x1, y1 = self._map_coords(i, -height / 2)
            x2, y2 = self._map_coords(i, height / 2)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(-height / 2, height / 2):
            x1, y1 = self._map_coords(-width / 2, i)
            x2, y2 = self._map_coords(width / 2, i)
            self.w.create_line(x1, y1, x2, y2)

    def update(self, field, particles):
        """
        Redraws the visualization with the specified field and particles state.
        """
        # Removes a gray square for any tiles have been aggregated.
        for aggregate in field.aggregates:
            for x in aggregate.particles:
                for y in aggregate.particles[x]:
                    self.w.delete(self.tiles[(x, y)])

        # Delete all existing particles.
        if self.particles:
            for particle in self.particles:
                self.w.delete(particle)
                self.master.update_idletasks()

        # Draw new particles
        self.particles = []
        for particle in particles:
            # skip the particle that are not in the field.
            if not field.isParticleInField(particle):
                continue

            # Draw the particle.
            x, y = particle.position.x, particle.position.y
            x1, y1 = self._map_coords(x - 0.08, y - 0.08)
            x2, y2 = self._map_coords(x + 0.08, y + 0.08)
            self.particles.append(self.w.create_oval(x1, y1, x2, y2, fill = "black"))
            self.particles.append(self._draw_particle(particle.position, particle.direction))

        # Update text
        self.w.delete(self.text)
        self.time += 1
        text = self._status_string(self.time, field.countAggregated())
        self.text = self.w.create_text(25, 0, anchor= NW, text = text)
        self.master.update()
        time.sleep(self.delay)

    def done(self):
        """
        Indicate that the animation is done so that we allow the user to close the window.
        """
        mainloop()
