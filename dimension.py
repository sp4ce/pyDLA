import math
import numpy
import pylab

from classes import *

class DimensionSimulation(Simulation):

    def __init__(self, width, height):
        Simulation.__init__(self, 1, width, height)
        self.lastSize = None
        self.sizes = []
        self.particles = []

    def callback(self):
        currentSize = self.field.aggregates[0].size()
        currentParticles = self.field.aggregates[0].count()
        if self.lastSize != None or currentSize != self.lastSize:
            self.lastSize = currentSize
            if currentSize != 0:
                self.sizes.append(currentSize)
                self.particles.append(currentParticles)

# The dimension is N(r) = k * r ** d
# so it is log(N) = d * log(r) + K

sizes = []
particles = []

for i in range(0, 10):
    simulation = DimensionSimulation(50, 50)
    simulation.animation = False
    simulation.run(StandardParticle, 20, 2000)
    sizes.extend(simulation.sizes)
    particles.extend(simulation.particles)

# Make the lin reg
x = map(math.log, sizes)
y = map(math.log, particles)
m, b = numpy.polyfit(x, y, 1)

# plot the noisy data
pylab.plot(sizes, particles, linestyle='', marker='.', label = 'Experiment data')

# Plot the lin reg
pylab.plot(sizes, math.exp(b) * numpy.array(sizes) ** m, label = "Dimension " + str(round(m, 2)))

# Add some legends
pylab.xlabel('Size of the aggregates')
pylab.ylabel('Number of particles')
pylab.title('Fractal dimension of the aggregate')
pylab.legend()

# Set the axes in log.
pylab.semilogy()
pylab.semilogx()

# Show the graph.
pylab.show()
