import time

from classes import *

import dla_visualize;

def simulation(seeds, speed, width, height, particle, num_particles, total_particles):
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
    anim_speed = 0.01
    anim = dla_visualize.Visualization(width, height, anim_speed)
    # time.sleep(5)

    # Initialize the room.
    f = Field(width, height, seeds)

    # Initialize the number of initial particles
    particles = []
    count = num_particles
    for i in range(0, num_particles):
        particles.append(particle(f, speed))

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
                    particles.append(particle(f, speed))
                    count += 1
                if p.aggregated:
                    update = True

        if update:
            # Update the animation only if the aggregate has changed
            if f.aggregateSize() > f.radius:
                # if the aggregate arrived to the radius size, we double the
                # size of the field and put the aggregate into this new field.
                width *= 2
                height *= 2
                new_f = Field(width, height)
                new_f.aggregates = f.aggregates
                f = new_f
                anim.init(width, height)

            anim.update(f, particles)

    anim.update(f, particles)
    anim.done()
