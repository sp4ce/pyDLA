import random

from classes import *

class TestParticle:

    def setup(self):
        self.field = Field(10, 10)
        self.particle = Particle(self.field, 1)

    def test_init(self):
        assert 0 <= self.particle.direction and self.particle.direction <= 360
        assert not self.field.isPositionOutsideDoubleRadius(self.particle.position)
        assert self.particle.valid
        assert not self.particle.aggregated

    def test_updatePositionAndAggregate(self):
        try:
            self.particle.updatePositionAndAggregate()
            assert False
        except NotImplementedError:
            assert True

class TestStandardParticle(TestParticle):

    def setup(self):
        self.field = Field(10, 10, 1)
        self.particle = StandardParticle(self.field, 1)

    def test_updatePositionAndAggregate(self):
        random.seed(0)
        self.particle = StandardParticle(self.field, 1)
        count = self.updatePositionAndAggregate()
        assert count == 20
        assert not self.particle.valid
        assert not self.particle.aggregated

        random.seed(1)
        self.particle = StandardParticle(self.field, 1)
        count = self.updatePositionAndAggregate()
        assert count == 29
        assert self.particle.valid
        assert self.particle.aggregated

    def updatePositionAndAggregate(self):
        count = 0
        while(self.particle.valid and not self.particle.aggregated):
            self.particle.updatePositionAndAggregate()
            count += 1
        return count
