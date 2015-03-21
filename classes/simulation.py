from animation import Animation
from field import Field

class Simulation:

    def __init__(self, seeds, width, height):
        """
        Initialize a simulation

        seeds: an int, the number of seeds in the field
        width: an int (width > 0)
        height: an int (height > 0)
        """
        # Save the parameters of the animation.
        self.seeds = seeds
        self.width = width
        self.height = height
        self.speed = 1
        self.animation = True
        self.steps = 0

        # Initialize the room.
        self.field = Field(width, height, seeds)

    def run(self, particle, num_particles, total_particles):
        """
        Run a diffusion limited aggregation simulation.

        seeds: an int, the number of seeds in the field
        speed: a float (speed > 0)
        width: an int (width > 0)
        height: an int (height > 0)
        particle: class of particle to be instantiated
        num_particles: an int, the number of particle present simultaneously
        total_particles: an int, the number of total particle to shoot.
        """
        # Initialize the animation.
        if self.animation:
            animation = Animation(self.width, self.height, 0.001)

        # Initialize the number of initial particles
        particles = []
        count = num_particles
        for i in range(0, num_particles):
            particles.append(particle(self.field, self.speed))

        # Initialize the time counter
        if self.animation:
            animation.update(self.steps, len(particles), count, self.field)

        # We run the simulation until all the particle has been created
        while count <= total_particles and 0 < len(particles):
            update = False
            for p in particles:
                # For each particle, update the position.
                p.updatePositionAndAggregate()
                if not p.valid or p.aggregated:
                    # Remove the particle from the sample if it is not valid.
                    particles.remove(p)
                    if count < total_particles:
                        # Add a new particle if there is some more place for it.
                        particles.append(particle(self.field, self.speed))
                        count += 1
                    if p.aggregated:
                        update = True

            # Increase the time counter
            self.steps += 1

            # Call the callback.
            self.callback()

            if update:
                # Update the animation only if the aggregate has changed
                if self.field.aggregateSize() > self.field.radius:
                    # if the aggregate arrived to the radius size, we double the
                    # size of the field and put the aggregate into this new field.
                    self.width *= 2
                    self.height *= 2
                    new_field = Field(self.width, self.height)
                    new_field.aggregates = self.field.aggregates
                    self.field = new_field
                    if self.animation:
                        animation.init(self.width, self.height)

                if self.animation:
                    animation.update(self.steps, len(particles), count, self.field)
            elif self.animation:
                animation.update(self.steps, len(particles), count)

        print "Done"
        if self.animation:
            animation.update(self.steps, len(particles), count, self.field)
            animation.done()

    def callback(self):
        pass
