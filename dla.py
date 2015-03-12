import time

from classes import *

import dla_visualize;

def simulation(seeds, speed, width, height, particule, num_particules, total_particules):
    """
    Run a diffusion limited aggregation simulation.

    seeds: an int, the number of seeds in the field
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    particule: class of particule to be instantiated
    num_particules: an int, the number of particule present simultaneously
    total_particules: an int, the number of total particule to shoot.
    """
    anim = dla_visualize.Visualization(width, height, 0.001)
    # time.sleep(5)

    # Initialize the room.
    f = Field(width, height, seeds)

    # Initialize the number of initial particules
    particules = []
    count = num_particules
    for i in range(0, num_particules):
        particules.append(particule(f, speed))

    # We run the simulation until all the particule has been created
    while count <= total_particules and 0 < len(particules):
        display = False
        for p in particules:
            # For each particule, update the position.
            p.updatePositionAndAggregate()
            if not p.valid or p.aggregated:
                # Remove the particule from the sample if it is not valid.
                particules.remove(p)
                if count < total_particules:
                    # Add a new particule if there is some more place for it.
                    particules.append(particule(f, speed))
                    count += 1
                if p.aggregated:
                    display = True

        if display:
            anim.update(f, particules)

    anim.done()

    print f.getNumAggregatedTiles() / float(f.getNumTiles())
