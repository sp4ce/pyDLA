import random

from classes import *

class ThunderParticle(StandardParticle):
	"""
	Try to modelize the thunder by saying that a particle
	has more probability to aggregate on the bottom.
	"""
	def aggregate(self):
		# If the particle is next to the aggregate, aggregate it.
		for aggregate in self.field.aggregates:
			for i in [-1, 0, 1]:
				for j in [-1, 0, 1]:
					if i == 0 and j == 0:
						# Do not test the current position.
						continue
					# Return True as soon as it finds an aggregated position.
					if aggregate.contains(Position(self.position.x + i, self.position.y + j)):
						# Get the probability of aggregation for the side of the particle.
						if j < 0:
							prob = 1 if i == 0 else 0.5
						elif j == 0:
							prob = 0.2
						else:
							prob = 0
						# Get a random number to see if the particle is added to the aggregate.
						if random.random() < prob:
							aggregate.add(self.position)
							self.aggregated = True
							return

simulation = Simulation(1, 50, 50)
simulation.run(ThunderParticle, 1000, 5000)